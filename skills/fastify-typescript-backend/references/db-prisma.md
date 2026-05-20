# Database — Prisma

## Install
```bash
bun add -d prisma @prisma/client
bunx prisma init
```

---

## `src/plugins/db.ts`
```typescript
import fp from 'fastify-plugin'
import { PrismaClient } from '@prisma/client'
import type { FastifyInstance } from 'fastify'

export default fp(async (fastify: FastifyInstance) => {
  const prisma = new PrismaClient()
  await prisma.$connect()

  fastify.decorate('db', prisma)

  fastify.addHook('onClose', async () => {
    await prisma.$disconnect()
  })
})
```

---

## `src/types/fastify.d.ts`
```typescript
import type { PrismaClient } from '@prisma/client'

declare module 'fastify' {
  interface FastifyInstance {
    db: PrismaClient
  }
  interface FastifyRequest {
    userId?: string
  }
}
```

---

## `package.json` scripts (add these)
```jsonc
{
  "db:generate": "bunx prisma generate",
  "db:migrate":  "bunx prisma migrate dev",
  "db:studio":   "bunx prisma studio"
}
```
