---
name: exec-pitch-generator
description: Generates a professional investment proposal and leadership pitch deck in Markdown format, designed to persuade executives and leadership to approve and fund a project. Reads from SDLC documents produced by sdlc-doc-generator (BRD, PRD, TDD, etc.) or any existing project documents. Use this skill whenever the user wants to pitch a project to leadership, create an executive summary, build a business case, request project funding or approval, or present a proposal to a CEO or leadership team. Also trigger when a tech team needs to justify a project before getting budget, when someone says "convince the executives", "get approval", "investment proposal", "pitch deck", or "business case". Works standalone or as a follow-up to sdlc-doc-generator.
---

# Executive Pitch Generator

Produces two persuasion-focused documents in Markdown format:

1. **Investment Proposal** (`InvestmentProposal_<ProjectName>.md`) — 1-2 page document making the case for funding, structured for easy copy-paste into Word or Google Docs
2. **Pitch Deck** (`PitchDeck_<ProjectName>.md`) — 6-8 slide content structured with clear page numbers, ready to copy-paste into PowerPoint, Google Slides, or Keynote slide by slide

Both files are plain Markdown — no dependencies, works in Claude.ai and Claude Code equally.

## Context: Why This Skill Exists

This skill is designed for **bottom-up project initiation** — where the tech or ops team identifies an opportunity or problem and must **pitch upward to get approval and funding**, BEFORE any budget or deadline has been committed. The documents are deliberately persuasive, not just informational.

This is the opposite of the traditional flow where executives approve a project first, then ask teams to document it.

---

## Workflow

### Phase 1 — Source Document Discovery

1. Ask the user for the folder path containing their SDLC documents (BRD, PRD, TDD, etc.) or any other project information they have.

2. Read all files in the folder:
   ```bash
   ls -la /path/to/folder
   cat /path/to/folder/*.md
   ```

3. Extract and map the following key information needed for the pitch:
   - **Problem** — what pain, inefficiency, or risk exists today
   - **Proposed solution** — what the project will build or change
   - **Business benefits** — efficiency gains, cost savings, risk reduction, revenue impact
   - **Investment required** — estimated cost, time, people, tools
   - **Timeline** — how long it will take, key milestones
   - **Risks of inaction** — what happens if the project is NOT approved
   - **Success metrics** — how results will be measured
   - **Stakeholders** — who benefits, who sponsors

---

### Phase 2 — Gap-Filling Questions

After reading the source documents, identify missing information and ask **only what is needed**. Focus on:

- Any estimated numbers not in the docs (cost savings, time saved, headcount affected)
- The main audience — who specifically will receive this pitch (CEO, CTO, Board, etc.)
- The preferred tone — conservative/formal vs bold/visionary
- Any constraints — budget ceiling, preferred timeline, political sensitivities

Keep questions to a maximum of 8. Never ask for information already in the source files.

---

### Phase 3 — Generate the Investment Proposal

Read `references/investment-proposal-template.md` before generating.

**Key principles:**
- Maximum 2 pages worth of content — executives will not read more
- Lead with the problem, not the solution
- Every section must answer "so what?" from a business perspective
- Use plain language — no technical jargon
- End with a single, unambiguous call-to-action
- Use Markdown tables for cost/benefit — executives scan, not read

**Formatting rules for easy copy-paste into Word:**
- Use `#` for the document title
- Use `##` for each section heading
- Use `>` blockquotes for the call-to-action or key emphasis lines
- Use tables for cost/benefit comparisons
- Use `-` bullet lists for benefits and risks
- Add a clear `---` divider between each section
- Add `<!-- END OF DOCUMENT -->` at the bottom

Save as: `InvestmentProposal_<ProjectName>.md`

---

### Phase 4 — Generate the Pitch Deck

Read `references/pitch-deck-template.md` before generating.

**Key principles:**
- 6-8 slides maximum — respect their time
- One message per slide
- Narrative arc: Pain → Possibility → Proposal → Payoff → Ask
- The final slide is THE ASK — make it impossible to misunderstand
- Write slide content as it should appear on the slide — concise, punchy, not paragraphs

**Formatting rules for easy copy-paste into PowerPoint slide by slide:**
- Start every slide with a divider and bold page label:
  ```
  ---
  **[ PAGE 1 of 8 ]**
  ```
- Follow immediately with the slide title using `#`
- Use `**Label:**` for any callout stats or key points
- Use short `-` bullet points (max 8 words each)
- Use a `> ` blockquote for the single most important line on each slide (the headline message)
- Use a table where a side-by-side comparison appears
- End every slide section with a `---` divider
- Add a `<!-- SPEAKER NOTES: -->` comment after each slide for optional speaker notes
- Add `<!-- END OF DECK -->` at the bottom

Save as: `PitchDeck_<ProjectName>.md`

---

### Phase 5 — Present and Offer Refinement

1. Save both files to `/mnt/user-data/outputs/` (Claude.ai) or current working directory (Claude Code)
2. Present both files to the user
3. Add a short note explaining:
   - The Investment Proposal is ready to copy-paste section by section into Word or Google Docs
   - The Pitch Deck is organised by page number — copy each page block into a new slide
4. Ask: *"Would you like to adjust the tone, rework any specific slide, or add more detail to any section?"*

---

## Tone & Language Guide

| Audience | Tone | Language |
|---|---|---|
| CEO / Board | Bold, concise, ROI-focused | Business outcomes only |
| CTO / VP Eng | Balanced — business + technical | Light technical context OK |
| CFO | Conservative, number-heavy | Cost/benefit, risk framing |
| Mixed leadership | Outcome-first, accessible | Zero jargon |

When in doubt, write for the least technical person in the room.

---

## Reference Files

- `references/investment-proposal-template.md` — section-by-section structure and writing guide for the proposal
- `references/pitch-deck-template.md` — slide-by-slide structure, content guide, and copy tips for the deck
