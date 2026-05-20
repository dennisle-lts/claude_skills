# RFC 9457 — Problem Details for HTTP APIs

All API errors use `Content-Type: application/problem+json`.

## Response shape

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | URI string | yes | Identifies the problem type. Use `about:blank` for standard HTTP errors, or a path like `/problems/validation-error` for custom types |
| `title` | string | yes | Short, stable summary of the problem type |
| `status` | number | yes | HTTP status code |
| `detail` | string | yes | Human-readable explanation specific to this occurrence |
| `instance` | URI string | no | URI identifying this specific occurrence (e.g. `/problems/log/abc-123`) |

Extension members (e.g. `errors` for validation details) are allowed.

---

## `src/shared/errors/app-error.ts`
```typescript
export interface ProblemDetails {
  type: string
  title: string
  status: number
  detail: string
  instance?: string
  [key: string]: unknown
}

export class AppError extends Error {
  readonly type: string
  readonly title: string
  readonly status: number
  readonly detail: string
  readonly instance?: string
  readonly extensions: Record<string, unknown>

  constructor(problem: ProblemDetails) {
    super(problem.detail)
    const { type, title, status, detail, instance, ...extensions } = problem
    this.type = type
    this.title = title
    this.status = status
    this.detail = detail
    this.instance = instance
    this.extensions = extensions
  }

  toProblemDetails(): ProblemDetails {
    return {
      type: this.type,
      title: this.title,
      status: this.status,
      detail: this.detail,
      ...(this.instance ? { instance: this.instance } : {}),
      ...this.extensions,
    }
  }
}
```

---

## `src/shared/errors/http-errors.ts`
```typescript
import { AppError } from './app-error'

export class NotFoundError extends AppError {
  constructor(detail: string, instance?: string) {
    super({ type: 'about:blank', title: 'Not Found', status: 404, detail, instance })
  }
}

export class UnauthorizedError extends AppError {
  constructor(detail = 'Authentication required', instance?: string) {
    super({ type: 'about:blank', title: 'Unauthorized', status: 401, detail, instance })
  }
}

export class ForbiddenError extends AppError {
  constructor(detail = 'Insufficient permissions', instance?: string) {
    super({ type: 'about:blank', title: 'Forbidden', status: 403, detail, instance })
  }
}

export class ConflictError extends AppError {
  constructor(detail: string, instance?: string) {
    super({ type: 'about:blank', title: 'Conflict', status: 409, detail, instance })
  }
}

export class UnprocessableEntityError extends AppError {
  constructor(detail: string, instance?: string) {
    super({ type: 'about:blank', title: 'Unprocessable Entity', status: 422, detail, instance })
  }
}

export class InternalServerError extends AppError {
  constructor(detail = 'An unexpected error occurred', instance?: string) {
    super({ type: 'about:blank', title: 'Internal Server Error', status: 500, detail, instance })
  }
}
```

---

## `src/hooks/on-error.ts`
```typescript
import type { FastifyError, FastifyInstance, FastifyReply, FastifyRequest } from 'fastify'
import { AppError } from '@shared/errors/app-error'

const PROBLEM_CONTENT_TYPE = 'application/problem+json'

export function registerErrorHook(fastify: FastifyInstance) {
  fastify.setErrorHandler((error: FastifyError | AppError | Error, req: FastifyRequest, reply: FastifyReply) => {
    // AppError subclasses — already shaped as RFC 9457
    if (error instanceof AppError) {
      return reply
        .status(error.status)
        .type(PROBLEM_CONTENT_TYPE)
        .send(error.toProblemDetails())
    }

    // Fastify/Zod validation errors (statusCode 400 with validation property)
    if ('validation' in error && error.validation) {
      return reply
        .status(400)
        .type(PROBLEM_CONTENT_TYPE)
        .send({
          type: '/problems/validation-error',
          title: 'Validation Error',
          status: 400,
          detail: 'One or more request fields failed validation.',
          errors: error.validation,
        })
    }

    // Fastify built-in HTTP errors (e.g. 404 route not found)
    if ('statusCode' in error && typeof error.statusCode === 'number') {
      return reply
        .status(error.statusCode)
        .type(PROBLEM_CONTENT_TYPE)
        .send({
          type: 'about:blank',
          title: error.name ?? 'HTTP Error',
          status: error.statusCode,
          detail: error.message,
        })
    }

    // Unhandled — log and return 500
    fastify.log.error(error)
    return reply
      .status(500)
      .type(PROBLEM_CONTENT_TYPE)
      .send({
        type: 'about:blank',
        title: 'Internal Server Error',
        status: 500,
        detail: 'An unexpected error occurred.',
      })
  })
}
```

Register inside `buildApp()` in `src/app.ts` after plugins, before modules:
```typescript
import { registerErrorHook } from './hooks/on-error'
// ...
registerErrorHook(app)
```

---

## Custom problem type example

Use a descriptive `type` URI when a problem deserves its own category:

```typescript
throw new AppError({
  type: '/problems/insufficient-balance',
  title: 'Insufficient Balance',
  status: 422,
  detail: 'Account balance is too low to complete the transfer.',
  instance: `/problems/log/${crypto.randomUUID()}`,
  currentBalance: 10,
  requiredBalance: 100,
})
```

Response:
```json
{
  "type": "/problems/insufficient-balance",
  "title": "Insufficient Balance",
  "status": 422,
  "detail": "Account balance is too low to complete the transfer.",
  "instance": "/problems/log/3fa85f64-...",
  "currentBalance": 10,
  "requiredBalance": 100
}
```
