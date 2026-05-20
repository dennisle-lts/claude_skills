---
name: fastify-typescript-backend
description: >
  Scaffold and extend a production-grade REST API using Fastify v5, TypeScript, Bun, and Zod.
  Use this skill whenever the user wants to: create a new Fastify backend project, add a new
  module/domain/endpoint to an existing one, wire up plugins, set up validation schemas, or
  follow the established project conventions. Trigger on phrases like "create a new API",
  "add a new endpoint", "scaffold a module", "set up Fastify", "create a route", "add a service",
  "generate a controller", or any request to build or extend a TypeScript/Fastify backend.
  Always use this skill for any Fastify + Bun + TypeScript task — even if the user only asks
  to add a single route or schema.
---

# Fastify v5 · TypeScript · Bun · Zod — Backend Skill

## Stack

| Concern | Tool |
|---|---|
| Runtime | **Bun** — runs TypeScript natively, no transpile step in dev |
| Framework | **Fastify v5** |
| Validation | **Zod v4** (`zod/v4`) + `fastify-type-provider-zod` |
| Linting + Formatting | **Biome** — replaces ESLint + Prettier |
| Database | **Prisma** (recommended), **Drizzle** |
| Testing | **`bun test`** — built-in, no extra deps |

---

## Workflow

### Starting a new project
Follow **Phase 1 → Phase 2 → Phase 3 → Phase 4** in order.

### Adding a module to an existing project
Jump directly to **Phase 3 — Module Pattern**, then update `src/app.ts`.

---

## Phase 1 — Database Choice

> **Always ask the user which database/ORM they prefer before scaffolding.** If unsure, recommend Prisma.

| Option | Best for |
|---|---|
| **Prisma** *(recommended)* | Schema-first, type-safe, great DX, built-in migration tooling |
| **Drizzle** | Lighter weight, SQL-like syntax, more control |

---

## Phase 2 — Project Scaffold

### 2.1 Init & Install

**With Prisma (recommended):**
```bash
mkdir my-api && cd my-api
bun init -y

bun add fastify fastify-plugin @fastify/cors @fastify/helmet \
        @fastify/jwt @fastify/rate-limit @fastify/swagger @fastify/swagger-ui \
        fastify-type-provider-zod zod

bun add -d @types/bun @biomejs/biome prisma @prisma/client
```

**With Drizzle:**
```bash
mkdir my-api && cd my-api
bun init -y

bun add fastify fastify-plugin @fastify/cors @fastify/helmet \
        @fastify/jwt @fastify/rate-limit @fastify/swagger @fastify/swagger-ui \
        fastify-type-provider-zod zod drizzle-orm postgres

bun add -d @types/bun @biomejs/biome drizzle-kit
```

> **Never install** `typescript`, `ts-node`, `tsx`, `eslint`, `prettier`, or `@types/node`.

### 2.2 Project Structure

```
my-api/
├── src/
│   ├── app.ts
│   ├── server.ts
│   ├── config/
│   │   └── env.ts
│   ├── plugins/
│   │   ├── db.ts
│   │   ├── jwt.ts
│   │   ├── cors.ts
│   │   ├── helmet.ts
│   │   ├── rate-limit.ts
│   │   └── swagger.ts
│   ├── hooks/
│   │   ├── on-request.ts
│   │   └── on-error.ts
│   ├── modules/
│   │   ├── health/
│   │   ├── auth/
│   │   └── users/
│   ├── shared/
│   │   ├── errors/
│   │   │   ├── app-error.ts
│   │   │   └── http-errors.ts
│   │   ├── middlewares/
│   │   │   └── authenticate.ts
│   │   └── utils/
│   │       ├── password.ts
│   │       └── pagination.ts
│   └── types/
│       ├── fastify.d.ts
│       └── index.ts
├── test/
│   ├── helpers/build-app.ts
│   └── modules/
├── prisma/           # Prisma only
├── .env
├── .env.example
├── biome.json
├── tsconfig.json
└── package.json
```

### 2.3 Write Core Files

Read `references/core-files.md` and write:
- `src/server.ts`
- `src/app.ts`
- `src/config/env.ts`
- `src/plugins/swagger.ts`
- `src/shared/utils/password.ts`
- `test/helpers/build-app.ts`

### 2.4 Write Database Files

- **Prisma:** read `references/db-prisma.md` and write `src/plugins/db.ts` and `src/types/fastify.d.ts`
- **Drizzle:** read `references/db-drizzle.md` and write `src/plugins/db.ts` and `src/types/fastify.d.ts`

### 2.5 Write Config Files

Read `references/config-files.md` and write `tsconfig.json` and `package.json`.

---

## Phase 3 — Module Pattern

Read `references/module-pattern.md` before creating any module.

Each module lives in `src/modules/<domain>/` and always has:
- `<domain>.schema.ts` — Zod schemas and inferred types
- `<domain>.routes.ts` — HTTP contract only
- `<domain>.controller.ts` — calls services, no logic
- `<domain>.service.ts` — business logic
- `<domain>.repository.ts` — all DB queries (only if module needs DB)
- `index.ts` — module plugin export wrapped with `fastify-plugin`

After creating the files, register the module in `src/app.ts` (import + `app.register`).

---

## Phase 4 — RFC 9457 Error Handling

Read `references/rfc9457-errors.md` before writing any error-related file.

All error responses **must** use `Content-Type: application/problem+json` and conform to [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457).

Files to create:
- `src/shared/errors/app-error.ts` — `AppError` base class with `toProblemDetails()`
- `src/shared/errors/http-errors.ts` — `NotFoundError`, `UnauthorizedError`, `ForbiddenError`, `ConflictError`, etc.
- `src/hooks/on-error.ts` — global Fastify error handler; normalises `AppError`, Zod validation errors, and Fastify HTTP errors

Register the hook in `src/app.ts` after plugins, before modules.

---

## Rules — Always Follow

| Rule | Detail |
|---|---|
| **No autoload** | All plugins and modules must be imported and registered explicitly in `src/app.ts` |
| **Swagger first** | `swaggerPlugin` must be registered before any route module |
| **Full Zod schemas** | Never use raw JSON schema. Always use Zod objects via `fastify-type-provider-zod` |
| **Types from schemas** | TypeScript types are always `z.infer<typeof SomeSchema>` — never written by hand |
| **No `any`** | Use `unknown` and narrow with Zod |
| **No logic in routes/controllers** | Routes = HTTP contract. Controllers = call services. Services = logic. Repositories = DB |
| **Plugins wrapped with `fp`** | All plugins must use `fastify-plugin` so decorators escape encapsulation |
| **Path aliases** | Use `@modules/`, `@shared/`, `@config/` — never deep relative paths |
| **`env` object only** | Never read `process.env` or `Bun.env` outside `src/config/env.ts` |
| **`app.listen()` object form** | Always `app.listen({ port, host })` — variadic args removed in Fastify v5 |
| **Bun built-ins** | Use `Bun.password.hash/verify`, `bun test`, `import.meta.dir` (not `__dirname`) |
| **RFC 9457 errors** | Never send a plain JSON error from a controller or service. Always throw an `AppError` subclass and let `on-error.ts` format it |
