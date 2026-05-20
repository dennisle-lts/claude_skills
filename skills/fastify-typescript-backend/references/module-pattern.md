# Module Pattern

Every domain lives in `src/modules/<domain>/` with this exact file set.
Replace `<domain>` (lowercase) and `<Domain>` (PascalCase) with the actual name.

---

## `<domain>.schema.ts` — Zod schemas (source of truth)
```typescript
import { z } from 'zod/v4'

export const Create<Domain>BodySchema = z.object({
  // define fields here
})

export const <Domain>ParamsSchema = z.object({
  id: z.string().uuid(),
})

export const <Domain>ResponseSchema = z.object({
  id: z.string().uuid(),
  // define response fields
  createdAt: z.string().datetime(),
})

export const <Domain>ListResponseSchema = z.array(<Domain>ResponseSchema)

// TypeScript types inferred from schemas — never written by hand
export type Create<Domain>Body = z.infer<typeof Create<Domain>BodySchema>
export type <Domain>Params     = z.infer<typeof <Domain>ParamsSchema>
export type <Domain>Response   = z.infer<typeof <Domain>ResponseSchema>
```

---

## `<domain>.routes.ts` — HTTP contract only
```typescript
import type { FastifyPluginAsyncZod } from 'fastify-type-provider-zod'
import { getAll, getById, create } from './<domain>.controller'
import {
  Create<Domain>BodySchema,
  <Domain>ParamsSchema,
  <Domain>ResponseSchema,
  <Domain>ListResponseSchema,
} from './<domain>.schema'

const <domain>Routes: FastifyPluginAsyncZod = async (fastify) => {
  fastify.get('/<domain>s', {
    schema: { response: { 200: <Domain>ListResponseSchema } },
    handler: getAll,
  })

  fastify.get('/<domain>s/:id', {
    schema: {
      params: <Domain>ParamsSchema,
      response: { 200: <Domain>ResponseSchema },
    },
    handler: getById,
  })

  fastify.post('/<domain>s', {
    schema: {
      body: Create<Domain>BodySchema,
      response: { 201: <Domain>ResponseSchema },
    },
    handler: create,
  })
}

export default <domain>Routes
```

---

## `<domain>.controller.ts` — Calls services, no business logic
```typescript
import type { FastifyRequest, FastifyReply } from 'fastify'
import type { Create<Domain>Body, <Domain>Params } from './<domain>.schema'
import * as <Domain>Service from './<domain>.service'

export async function getAll(_req: FastifyRequest, reply: FastifyReply) {
  const items = await <Domain>Service.findAll()
  return reply.send(items)
}

export async function getById(
  req: FastifyRequest<{ Params: <Domain>Params }>,
  reply: FastifyReply,
) {
  const item = await <Domain>Service.findById(req.params.id)
  return reply.send(item)
}

export async function create(
  req: FastifyRequest<{ Body: Create<Domain>Body }>,
  reply: FastifyReply,
) {
  const item = await <Domain>Service.create(req.body)
  return reply.status(201).send(item)
}
```

---

## `<domain>.service.ts` — Business logic only
```typescript
import type { Create<Domain>Body } from './<domain>.schema'

export async function findAll() {
  // call repository
}

export async function findById(id: string) {
  // call repository
}

export async function create(data: Create<Domain>Body) {
  // validate, transform, call repository
}
```

---

## `<domain>.repository.ts` — All DB queries (include only when module needs DB)
```typescript
import type { FastifyInstance } from 'fastify'
// All Prisma/Drizzle queries for this domain live here
// Access fastify.db via dependency injection or import the client directly
```

---

## `index.ts` — Module plugin export (always required)
```typescript
import fp from 'fastify-plugin'
import <domain>Routes from './<domain>.routes'

export default fp(<domain>Routes, {
  name: '<domain>-module',
})
```

---

## Register in `src/app.ts`

After creating the module files, add two lines to `src/app.ts`:

```typescript
// 1. Add import at the top with other module imports
import <domain>Module from './modules/<domain>'

// 2. Add register call in the modules block
await app.register(<domain>Module, { prefix: '/api/v1' })
```
