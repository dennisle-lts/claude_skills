# claude_skills

A personal collection of Claude Skills I've built and use day-to-day — shared with the community for anyone to use, or fork.

---

## What Are Claude Skills?

Skills extend Claude's capabilities by giving it access to specialised knowledge and workflows. Each skill is a folder containing a `SKILL.md` file with instructions, and optionally scripts, templates, and reference documents.

Skills work in both **Claude.ai** and **Claude Code**.

---

## Skills in This Collection

| Skill | Description |
|-------|-------------|
| [`sdlc-doc-generator`](./skills/sdlc-doc-generator/) | Generates BRD, PRD, TDD, Deployment Plan, Release Notes, and ADR documents in Markdown from your project information |
| [`exec-pitch-generator`](./skills/exec-pitch-generator/) | Generates a Word investment proposal and PowerPoint pitch deck to get a project approved by executives |
| [`web-expert`](./skills/web-expert/) | Full-stack Next.js 16.2 + shadcn/ui expert — scaffolding, components, App Router, Server Actions, and more |

---

## Installation

### Claude.ai

1. Download the `.skill` file for the skill you want
2. Go to **Customize → Skills** and upload the file
3. Make sure **Code execution and file creation** is enabled under **Settings → Capabilities**

> Requires a **Pro, Max, Team, or Enterprise** plan.

### Claude Code

Skills in Claude Code are folder-based. Copy the skill folder to your skills directory:

```bash
# Personal — available across all projects
cp -r <skill-folder> ~/.claude/skills/

# Project-level — available in one project only
cp -r <skill-folder> your-project/.claude/skills/
```

---

## Skill Structure

Every skill follows this structure:

```
skill-name/
├── SKILL.md           # Required — YAML frontmatter + instructions
├── references/        # Optional — templates, guides, reference docs
├── scripts/           # Optional — executable helper scripts
└── assets/            # Optional — fonts, icons, static files
```

The `SKILL.md` frontmatter requires at minimum:

```yaml
---
name: skill-name
description: What this skill does and when Claude should use it.
---
```

---

## Resources

- [Anthropic Skills Documentation](https://docs.claude.com)
- [anthropics/skills](https://github.com/anthropics/skills) — official Anthropic skills repository
- [Claude Code Skills Guide](https://code.claude.com/docs/en/skills)

---

## License

MIT