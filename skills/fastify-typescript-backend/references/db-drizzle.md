# Database — Drizzle

## Install
```bash
bun add drizzle-orm postgres
bun add -d drizzle-kit
```

---

## `src/plugins/db.ts`
```typescript
import fp from 'fastify-plugin'
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'
import type { FastifyInstance } from 'fastify'
import { env } from '@config/env'

export default fp(async (fastify: FastifyInstance) => {
  const client = postgres(env.DATABASE_URL)
  const db = drizzle(client)

  fastify.decorate('db', db)

  fastify.addHook('onClose', async () => {
    await client.end()
  })
})
```

---

## `src/types/fastify.d.ts`
```typescript
import type { PostgresJsDatabase } from 'drizzle-orm/postgres-js'

declare module 'fastify' {
  interface FastifyInstance {
    db: PostgresJsDatabase
  }
  interface FastifyRequest {
    userId?: string
  }
}
```
