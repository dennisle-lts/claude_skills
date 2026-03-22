---
name: web-expert
description: >
  Use this skill for any task involving Next.js or shadcn/ui — scaffolding projects, adding UI
  components, building pages, configuring themes, using Server Components or Server Actions, setting
  up the App Router, understanding Next.js 16.2 AI agent features, or anything full-stack React/Next.
  Trigger for phrases like "set up a Next.js project", "add a shadcn component", "init shadcn",
  "create a page with a card and button", "my agent keeps starting duplicate dev servers", or any
  Next.js / React / UI library question. This skill always uses the shadcn CLI (never hand-writes
  component code), always asks the user to choose a color scheme before init, and defaults to
  shadcn's built-in styles — custom CSS only when the user explicitly requests it.
---

# Web Expert — Next.js 16.2 + shadcn/ui

---

## Step 0 — Ask Color Scheme Before Anything Else

Before running `shadcn init`, ask the user to choose their base color and visual style. These are
selected during the interactive `init` prompts — there's no CLI flag for the color itself. Getting
this right upfront matters because changing it later means rewriting `globals.css` and
`components.json`.

**Base color** (chosen interactively during `init`):

| Value | Character |
|-------|-----------|
| `neutral` | Pure grays — the classic shadcn default |
| `stone` | Warm, slightly brownish grays |
| `zinc` | Cool, blue-tinted grays |
| `mauve` | Subtle purple-gray tones |
| `olive` | Muted green-gray tones |
| `mist` | Soft, cool blue-gray tones |
| `taupe` | Warm, earthy beige-gray tones |

**Visual style** (also chosen interactively — default is Vega):

| Style | Character |
|-------|-----------|
| Vega | Classic shadcn — clean and neutral **(default)** |
| Nova | Reduced padding for compact layouts |
| Maia | Soft and rounded with generous spacing |
| Lyra | Boxy and sharp — pairs well with mono fonts |
| Mira | Very compact — made for dense interfaces |

---

## Scaffolding

### Create a new Next.js project
```bash
# npm
npx create-next-app@latest

# pnpm
pnpm create next-app@latest

# yarn
yarn create next-app@latest

# bun
bun create next-app@latest

# upgrade existing project
npx @next/codemod@canary upgrade latest
```

### Init shadcn

Run the interactive init — it will prompt for base color, style, and other settings:

```bash
# npm
npx shadcn@latest init

# pnpm
pnpm dlx shadcn@latest init

# yarn
yarn dlx shadcn@latest init

# bun
bunx --bun shadcn@latest init
```

`create` is an alias for `init` — both work the same way.

**Useful init flags:**

| Flag | Purpose |
|------|---------|
| `-t, --template <name>` | Framework hint: `next`, `vite`, `react-router`, `laravel`, `astro` |
| `-b, --base <lib>` | Component library: `radix` (default) or `base` (Base UI) |
| `-d, --defaults` | Skip all prompts, use defaults |
| `-f, --force` | Overwrite existing config |
| `--monorepo` | Scaffold as a monorepo |
| `--reinstall` | Re-install already-installed components |
| `--rtl` | Enable right-to-left support |

> Note: `--base` here selects the **component library** (Radix UI vs Base UI primitives), NOT the
> color scheme. Color is selected interactively.

### Package manager detection

Check the lockfile before running any shadcn command:

| Lockfile | shadcn command prefix |
|----------|-----------------------|
| `package-lock.json` | `npx shadcn@latest` |
| `pnpm-lock.yaml` | `pnpm dlx shadcn@latest` |
| `yarn.lock` | `yarn dlx shadcn@latest` |
| `bun.lockb` / `bun.lock` | `bunx --bun shadcn@latest` |

If uncertain, ask the user.

---

## Adding shadcn Components — Always via CLI

shadcn's philosophy is that components live *in your codebase*, not inside `node_modules`. The CLI
ensures they land in the right path with the correct imports and dependencies wired up. Hand-writing
them skips all of that and leads to path alias mismatches and missing deps.

```bash
# Add a single component (npm)
npx shadcn@latest add button

# Add multiple at once
npx shadcn@latest add button card dialog sidebar

# Add with pnpm / yarn / bun
pnpm dlx shadcn@latest add button
yarn dlx shadcn@latest add button
bunx --bun shadcn@latest add button

# Overwrite an existing component
npx shadcn@latest add button --overwrite

# Preview what would change before writing files
npx shadcn@latest add button --dry-run

# Show a diff against the existing file
npx shadcn@latest add button --diff

# Show full file contents without installing
npx shadcn@latest add button --view

# Install to a custom path instead of the default ui/ directory
npx shadcn@latest add button --path src/components/shared

# Add all available components (use sparingly)
npx shadcn@latest add --all
```

### Inspect before installing

```bash
# View a component's full source before adding it
npx shadcn@latest view button

# View multiple at once
npx shadcn@latest view button card dialog

# View from a namespaced registry
npx shadcn@latest view @acme/auth @v0/dashboard
```

### Search registries

```bash
# Search the shadcn registry
npx shadcn@latest search @shadcn

# Search with a keyword filter
npx shadcn@latest search @shadcn -q "button"

# Search multiple registries
npx shadcn@latest search @shadcn @v0 @acme

# list is an alias for search
npx shadcn@latest list @shadcn
```

### Other useful commands

```bash
# Get docs + API reference for a component
npx shadcn@latest docs button

# Show installed components and full project config
npx shadcn@latest info

# Build registry JSON files (for custom registries)
npx shadcn@latest build
```

### Migrate existing components

The `migrate` command updates your installed component files in-place — useful after major shadcn upgrades or moving to a new primitive library:

```bash
# Migrate icon imports to a different icon library
npx shadcn@latest migrate icons

# Switch from individual @radix-ui/react-* packages to the unified radix-ui package
npx shadcn@latest migrate radix

# Add RTL support — converts physical CSS classes to logical equivalents (ml-4 → ms-4)
npx shadcn@latest migrate rtl

# Target a specific file or glob instead of the whole ui/ directory
npx shadcn@latest migrate radix src/components/ui/dialog.tsx
npx shadcn@latest migrate rtl "src/components/ui/**"

# See all available migrations
npx shadcn@latest migrate --list
```

### Recipe components — use docs, not just `add`

Some shadcn components are **recipes** rather than single installable files — they require reading
the docs page and wiring things up manually. When the user asks for one of these, run
`npx shadcn@latest docs <name>` first to get the full guide:

- **Data Table** — needs `@tanstack/react-table` + custom column/row setup
- **Combobox** — built from Command + Popover primitives
- **Date Picker** — Calendar + Popover + state wiring
- **Form** — needs `react-hook-form` or `@tanstack/react-form` integration

---

## Theming

shadcn's CSS variables give you a complete semantic colour system out of the box. Resist the urge
to add custom colours — if you override `--primary` you lose coherent dark mode and component
contrast ratios for free.

```tsx
// ✅ Use shadcn semantic classes — dark mode and contrast just work
<div className="bg-background text-foreground border border-border rounded-lg p-4">
<button className="bg-primary text-primary-foreground hover:bg-primary/90">

// ❌ Hardcoded values break dark mode and theming
<div style={{ backgroundColor: '#1a1a2e' }}>
<div className="bg-[#0f172a]">
```

Only write custom CSS when the user explicitly requests it.

---

## Next.js 16.2 — Key Facts

- **Version:** 16.2.0 (March 18, 2026)
- **Bundler:** Turbopack (stable default since Next.js 16)
- **React:** 19.2 — View Transitions, `useEffectEvent`, `<Activity>`, React Compiler (stable)
- **Router:** App Router only — Pages Router is legacy. All files go under `/app`.
- **Config:** `next.config.ts` (TypeScript native)
- **Middleware:** `proxy.ts` replaces `middleware.ts`

### App Router file conventions
```
app/
├── layout.tsx       # Root layout (required)
├── page.tsx         # Route page
├── error.tsx        # Error boundary — use unstable_retry() for data fetch errors
├── loading.tsx      # Suspense fallback
├── not-found.tsx    # 404
├── global-error.tsx # Top-level catch-all
└── (group)/page.tsx # Route groups — no URL segment
```

### Server vs Client Components
```tsx
// Server Component — the default, no directive needed
// Can: fetch data, access DB/secrets, use async/await
// Cannot: useState, useEffect, event handlers
export default async function Page() {
  const data = await db.query('SELECT * FROM products')
  return <ProductList items={data} />
}

// Client Component — add directive at top of file
'use client'
import { useState } from 'react'
export default function Counter() {
  const [n, setN] = useState(0)
  return <button onClick={() => setN(n + 1)}>{n}</button>
}
```

Push `'use client'` as deep as possible. Most pages can be 80%+ server-rendered — this reduces
client bundle size and improves Core Web Vitals scores directly.

### Server Actions
```tsx
// app/actions.ts
'use server'
export async function saveItem(formData: FormData) {
  await db.insert({ name: formData.get('name') })
  revalidateTag('items')
}

// In a Server Component form
<form action={saveItem}>
  <input name="name" />
  <button type="submit">Save</button>
</form>
```

In dev (16.2+), every Server Function execution is logged to the terminal with function name, args,
timing, and source file — so you can see exactly when and how they fire.

### Caching
```tsx
// Opt in explicitly with 'use cache' — replaces ISR and implicit caching
'use cache'
export async function getProducts() {
  return await db.query('...')
}
// Invalidate with:
revalidateTag('products')
updateTag('products')
```

### Partial Prerendering (PPR)
```tsx
// Static shell from edge instantly, dynamic content streams in after
import { Suspense } from 'react'
export default function Page() {
  return (
    <>
      <StaticShell />
      <Suspense fallback={<Skeleton />}>
        <DynamicFeed />
      </Suspense>
    </>
  )
}
```

---

## Next.js 16.2 — AI Agent Features

These features exist specifically because AI coding agents are now first-class users of the
framework. Use them to make agent-assisted development smoother.

### AGENTS.md
`create-next-app` auto-generates `AGENTS.md` at the project root, pointing agents to bundled
Next.js docs at `node_modules/next/dist/docs/`. Vercel research found this always-available
context achieved a **100% pass rate** on Next.js evals vs 79% with on-demand retrieval.

For existing 16.2+ projects without it, create `AGENTS.md` manually pointing to that path.

### Browser log forwarding
Client errors are forwarded to the terminal by default — agents without browser access see them.
```ts
// next.config.ts
logging: {
  browserToTerminal: 'error', // 'error' | 'warn' | true | false
}
```

### Dev server lock file
When `next dev` starts, it writes PID/port/URL to `.next/dev/lock`. A second start gets:
```
Error: Another next dev server is already running.
- Local: http://localhost:3000
- PID:   12345
Run kill 12345 to stop it.
```
This stops agents from spawning duplicate servers unknowingly.

### next-browser (experimental agent DevTools)
```bash
npx skills add vercel-labs/next-browser   # install
/next-browser                             # invoke in Claude Code or Cursor
```
Agents can then query a running app without touching a browser:
```bash
next-browser tree       # component tree: props, hooks, state, source locations
next-browser screenshot # visual snapshot
next-browser logs       # console + network
next-browser errors     # errors + PPR shell boundaries
```

### DevTools MCP
```json
// .mcp.json — enables natural-language upgrades + diagnostics
{
  "mcpServers": {
    "next-devtools": {
      "command": "npx",
      "args": ["-y", "next-devtools-mcp@latest"]
    }
  }
}
```

---

## Project Structure

```
my-app/
├── AGENTS.md               # agent docs context (16.2 auto-generates this)
├── next.config.ts
├── proxy.ts                # network boundary (replaces middleware.ts)
├── app/
│   ├── layout.tsx          # root layout + providers
│   ├── page.tsx            # home — Server Component by default
│   ├── actions.ts          # 'use server' mutations
│   ├── globals.css         # shadcn CSS variables
│   └── (routes)/
├── components/
│   ├── ui/                 # shadcn — managed by CLI only, don't edit manually
│   └── ...                 # your components
└── lib/
    └── utils.ts            # shadcn cn() utility
```

---

## Workflow Cheatsheet

| Task | npm | pnpm | bun |
|------|-----|------|-----|
| New project | `npx create-next-app@latest` | `pnpm create next-app@latest` | `bun create next-app@latest` |
| Upgrade Next.js | `npx @next/codemod@canary upgrade latest` | same | same |
| Init shadcn | `npx shadcn@latest init` | `pnpm dlx shadcn@latest init` | `bunx --bun shadcn@latest init` |
| Add component | `npx shadcn@latest add button` | `pnpm dlx shadcn@latest add button` | `bunx --bun shadcn@latest add button` |
| View component | `npx shadcn@latest view button` | `pnpm dlx shadcn@latest view button` | `bunx --bun shadcn@latest view button` |
| Component docs | `npx shadcn@latest docs button` | `pnpm dlx shadcn@latest docs button` | `bunx --bun shadcn@latest docs button` |
| Search registry | `npx shadcn@latest search @shadcn` | `pnpm dlx shadcn@latest search @shadcn` | `bunx --bun shadcn@latest search @shadcn` |
| Project info | `npx shadcn@latest info` | `pnpm dlx shadcn@latest info` | `bunx --bun shadcn@latest info` |
| Agent DevTools | `npx skills add vercel-labs/next-browser` | — | — |
| Debug production | `next start --inspect` | — | — |
