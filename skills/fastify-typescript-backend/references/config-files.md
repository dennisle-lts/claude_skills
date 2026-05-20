# Config Files

## `tsconfig.json`
```jsonc
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "lib": ["ESNext"],
    "types": ["bun-types"],
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "baseUrl": ".",
    "paths": {
      "@modules/*": ["src/modules/*"],
      "@shared/*":  ["src/shared/*"],
      "@config/*":  ["src/config/*"]
    }
  },
  "include": ["src", "test"],
  "exclude": ["node_modules", "dist"]
}
```

---

## `package.json`
```jsonc
{
  "name": "my-api",
  "type": "module",
  "scripts": {
    "dev":        "bun run --watch src/server.ts",
    "start":      "bun run src/server.ts",
    "build":      "bun build src/server.ts --outdir dist --target bun",
    "test":       "bun test",
    "test:watch": "bun test --watch",
    "lint":       "biome check src test",
    "lint:fix":   "biome check --write src test",
    "format":     "biome format --write src test",
    "typecheck":  "tsc --noEmit"
  }
}
```

---

## Biome init
```bash
bunx biome init
```

Biome replaces both ESLint and Prettier. Never install `eslint`, `prettier`, `typescript`, `ts-node`, or `tsx`.
