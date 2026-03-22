# Pitch Deck — Structure & Writing Guide

## Deck Rules
- 6-8 slides maximum
- One core message per slide
- Narrative arc: Pain → Possibility → Proposal → Payoff → Ask
- Write content as it appears ON the slide — short, punchy, not paragraphs
- Every slide has a single headline message (use blockquote `>`)
- Speaker notes are optional but encouraged — add after each slide as a comment

---

## Output Format

Each slide block follows this exact pattern:

```
---
**[ PAGE N of TOTAL ]** — [SLIDE THEME IN CAPS]

# [Slide Title]

> [The single most important line on this slide — the headline message]

[Content — bullets, table, or callout stats depending on slide type]

<!-- SPEAKER NOTES: [Optional notes for the presenter] -->
```

Always use `---` to open and close each slide block so the user knows exactly where one slide ends and the next begins.

---

## Slide-by-Slide Guide

Below is the exact Markdown structure to follow when generating `PitchDeck_<ProjectName>.md`.

---

```markdown
<!-- ============================================================ -->
<!-- PITCH DECK: [Project Name]                                   -->
<!-- Prepared by: [Name] | Date: [DD MMM YYYY]                   -->
<!-- Audience: [e.g. Executive Leadership Team]                  -->
<!-- ============================================================ -->

---
**[ PAGE 1 of 8 ]** — TITLE

# [Project Name]

> [One-line tagline — the entire pitch in a single sentence]

**Presented by:** [Name, Role]
**Date:** [DD MMM YYYY]

<!-- SPEAKER NOTES: Open with a brief personal introduction and why this matters now. -->

---
**[ PAGE 2 of 8 ]** — THE PROBLEM

# The Problem We're Solving

> [The single most painful and specific statement about the current situation]

- **[Pain point 1]:** [One line — specific and quantified where possible]
- **[Pain point 2]:** [One line]
- **[Pain point 3]:** [One line]

**Today this costs us:** [Key stat or impact — e.g. "~X hours per quarter" or "2x industry failure rate"]

<!-- SPEAKER NOTES: Spend time here. Make the audience feel the pain before moving on. Use real examples if available. -->

---
**[ PAGE 3 of 8 ]** — THE OPPORTUNITY

# What Becomes Possible

> [An aspirational statement about what changes if this project is approved]

- [Opportunity 1 — what improves]
- [Opportunity 2 — what becomes possible]
- [Opportunity 3 — what risk is removed]

| Today | After This Project |
|-------|-------------------|
| [Current state 1] | [Future state 1] |
| [Current state 2] | [Future state 2] |
| [Current state 3] | [Future state 3] |

<!-- SPEAKER NOTES: Shift the energy here — from pain to possibility. Keep it concrete, not vague. -->

---
**[ PAGE 4 of 8 ]** — OUR PROPOSAL

# What We're Proposing

> [Two-sentence summary of the solution — what it is and what it delivers]

**Phase 1 — [Name]** *(Month 1-2)*
[One line on what this phase delivers]

**Phase 2 — [Name]** *(Month 3-4)*
[One line on what this phase delivers]

**Phase 3 — [Name]** *(Month 5-6)*
[One line on what this phase delivers]

<!-- SPEAKER NOTES: Keep the focus on outcomes per phase, not tasks. Avoid technical detail here. -->

---
**[ PAGE 5 of 8 ]** — ROI & BENEFITS

# What the Business Gains

> [The single most compelling benefit — the number that makes them lean forward]

**[Stat 1]** — [Label, e.g. "↓ 67% onboarding time"]
**[Stat 2]** — [Label, e.g. "£X saved per quarter"]
**[Stat 3]** — [Label, e.g. "0 audit failures"]
**[Stat 4]** — [Label, e.g. "2 weeks to first value"]

[One sentence connecting these benefits back to the business strategy or a known leadership priority]

<!-- SPEAKER NOTES: If you have ranges rather than exact numbers, that's fine — say "we estimate" and explain the basis. -->

---
**[ PAGE 6 of 8 ]** — INVESTMENT & TIMELINE

# Investment Required

> [Payback statement — e.g. "Expected to pay back within X months of go-live"]

| Item | Estimate |
|------|----------|
| Internal team effort | [X person-days] |
| Tooling / software | [Cost or None] |
| External support | [Cost or None] |
| **Total** | **[Total]** |

**Key milestones:**
- [Date]: [Milestone 1]
- [Date]: [Milestone 2]
- [Date]: [Milestone 3 — go-live]

<!-- SPEAKER NOTES: Be transparent about costs. Always anchor with the payback statement. -->

---
**[ PAGE 7 of 8 ]** — RISK OF INACTION

# What Happens If We Don't Act

> [The starkest, most honest statement about the cost of doing nothing]

- **[Risk 1]:** [Specific consequence]
- **[Risk 2]:** [Specific consequence]
- **[Risk 3]:** [Specific consequence]

**Every quarter we delay:** [Cost or impact of delay — e.g. "costs approximately X in rework and lost productivity"]

<!-- SPEAKER NOTES: This slide is intentionally uncomfortable. Don't rush past it. Let it land. -->

---
**[ PAGE 8 of 8 ]** — THE ASK

# Our Recommendation

> [The ask — one sentence stating exactly what is needed from this room, today]

**We are seeking:**
- [Approval / funding amount / resource commitment]
- [Any secondary request — e.g. executive sponsor, timeline flexibility]

**If approved by [date], we can:**
- Begin [first milestone] by [date]
- Deliver [key outcome] by [date]

**Next step:** [What happens immediately after this meeting if they say yes]

**Contact:** [Name, email]

<!-- SPEAKER NOTES: End with silence and eye contact. Don't rush to "any questions?" — let THE ASK be the last thing they hear. -->

<!-- END OF DECK -->
```

---

## Content Tips Per Slide

### Page 1 — Title
The tagline is the most important line in the deck. It should make someone who only reads that one line understand exactly what you're asking for and why it matters. Draft 3 versions and pick the strongest.

### Page 2 — The Problem
Lead with the most specific, quantified pain point you have. Vague problems get vague responses. "Our deployments fail" is weak. "Our deployments fail at 2x the industry average, causing 3-4 hours of unplanned downtime per incident" is strong.

### Page 3 — The Opportunity
The before/after table is optional but powerful. Keep the "After" column realistic — don't overpromise.

### Page 4 — Our Proposal
Three phases works well for most projects. If the project is shorter, use two. Never use more than four — it signals poor planning.

### Page 5 — ROI & Benefits
Stats as callouts work better than bullets here. If you're copying into PowerPoint, make these numbers huge (48-60pt). The goal is that someone glancing at this slide for 3 seconds takes away one number.

### Page 6 — Investment & Timeline
Never hide costs. Pair the cost table immediately with the payback statement — the two belong together.

### Page 7 — Risk of Inaction
This is optional but highly effective for borderline decisions. Omit it if the audience is already sold and you don't want to create unnecessary anxiety.

### Page 8 — The Ask
The ask must be specific. Not "support for this project" but "approval to proceed and a budget of £X." Make it impossible to leave the room without knowing what decision was needed.
