# Core Files

## `src/server.ts`
```typescript
import { buildApp } from './app'
import { env } from './config/env'

const app = await buildApp()

await app.listen({
  port: env.PORT,
  host: env.HOST,
})
```

---

## `src/app.ts`
```typescript
import Fastify from 'fastify'
import { env } from './config/env'

// Plugins
import swaggerPlugin from './plugins/swagger'
import dbPlugin from './plugins/db'
import jwtPlugin from './plugins/jwt'
import corsPlugin from './plugins/cors'
import helmetPlugin from './plugins/helmet'
import rateLimitPlugin from './plugins/rate-limit'

// Hooks
import { registerErrorHook } from './hooks/on-error'

// Modules
import healthModule from './modules/health'
import authModule from './modules/auth'
import usersModule from './modules/users'

export async function buildApp() {
  const app = Fastify({
    logger: { level: env.LOG_LEVEL },
  })

  // Plugins — swagger MUST come first so setValidatorCompiler fires before routes
  await app.register(swaggerPlugin)
  await app.register(dbPlugin)
  await app.register(jwtPlugin)
  await app.register(corsPlugin)
  await app.register(helmetPlugin)
  await app.register(rateLimitPlugin)

  // Global error hook — must be registered after plugins, before modules
  registerErrorHook(app)

  // Modules — each prefixed with /api/v1
  await app.register(healthModule, { prefix: '/api/v1' })
  await app.register(authModule, { prefix: '/api/v1' })
  await app.register(usersModule, { prefix: '/api/v1' })

  return app
}
```

> **Critical:** Every new plugin goes in the plugins block. Every new module goes in the modules block. Never use `@fastify/autoload`.

---

## `src/config/env.ts`
```typescript
import { z } from 'zod/v4'

const EnvSchema = z.object({
  NODE_ENV: z.enum(['development', 'test', 'production']).default('development'),
  PORT: z.coerce.number().default(3000),
  HOST: z.string().default('127.0.0.1'),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  LOG_LEVEL: z.enum(['fatal', 'error', 'warn', 'info', 'debug', 'trace']).default('info'),
})

export const env = EnvSchema.parse(process.env)
export type Env = z.infer<typeof EnvSchema>
```

> **Rule:** Never read `process.env` or `Bun.env` directly outside this file.

---

## `src/plugins/swagger.ts`
```typescript
import fp from 'fastify-plugin'
import swagger from '@fastify/swagger'
import swaggerUi from '@fastify/swagger-ui'
import { jsonSchemaTransform, serializerCompiler, validatorCompiler } from 'fastify-type-provider-zod'

export default fp(async (fastify) => {
  fastify.setValidatorCompiler(validatorCompiler)
  fastify.setSerializerCompiler(serializerCompiler)

  await fastify.register(swagger, {
    openapi: {
      info: { title: 'My API', version: '1.0.0' },
    },
    transform: jsonSchemaTransform,
  })

  await fastify.register(swaggerUi, {
    routePrefix: '/documentation',
  })
})
```

---

## `src/shared/utils/password.ts`
```typescript
// Bun.password uses bcrypt natively — no bcryptjs needed
export async function hashPassword(plain: string): Promise<string> {
  return Bun.password.hash(plain)
}

export async function verifyPassword(plain: string, hash: string): Promise<boolean> {
  return Bun.password.verify(plain, hash)
}
```

---

## `test/helpers/build-app.ts`
```typescript
import { buildApp } from '../../src/app'

export async function createTestApp() {
  const app = await buildApp()
  await app.ready()
  return app
}
```
