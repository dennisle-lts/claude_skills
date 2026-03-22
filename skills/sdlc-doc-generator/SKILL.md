---
name: sdlc-doc-generator
description: Generates professional SDLC documents in Markdown format — BRD, PRD, TDD, Deployment Plan, Release Notes, and ADR — by reading source files from a user-provided folder and asking follow-up questions to fill any gaps. Use this skill whenever the user wants to create, generate, draft, or produce any software project documentation, requirements documents, technical documents, or IT project docs. Trigger even if the user only mentions one document type (e.g., "create a BRD" or "write a deployment plan") or asks to "document a project". Always use this skill for any combination of BRD, PRD, TDD, ADR, deployment plan, or release notes generation.
---

# SDLC Document Generator

Generates the following documents in Markdown (.md) format from source project information:
- **BRD** — Business Requirements Document
- **PRD** — Product Requirements Document
- **TDD** — Technical Design Document
- **Deployment Plan**
- **Release Notes**
- **ADR** — Architecture Decision Record

---

## Workflow

### Phase 1 — Source Information Gathering

1. Ask the user to provide the **folder path** that contains any existing project information. This could include:
   - Existing docs (Word, PDF, MD, TXT)
   - Meeting notes
   - Email exports
   - Spreadsheets
   - Wireframes descriptions
   - Any other reference material

2. **Read all files** in the folder using `bash_tool`:
   ```bash
   ls -la /path/to/folder
   cat /path/to/folder/*.md  # or txt, etc.
   ```

3. **Analyze the content** and map what you've found to the required sections of each document.

4. Build an internal **information gap list** — what is missing or unclear per document.

---

### Phase 2 — Follow-up Questions

After reading the folder, ask targeted follow-up questions **only for information that is missing** and cannot be reasonably inferred.

Group questions by theme to avoid overwhelming the user. Example groupings:
- Business context (for BRD gaps)
- Product & user details (for PRD gaps)
- Technical decisions (for TDD & ADR gaps)
- Release & deployment details (for Deployment Plan & Release Notes gaps)

**Important rules:**
- Never ask for information already present in the source files
- Ask a maximum of 10 questions at a time
- Prefer multiple choice or short answers where possible
- If a detail is minor and can be inferred, make a reasonable assumption and note it in the document

---

### Phase 3 — Document Generation

Generate each requested document as a separate `.md` file. Save all files to the **same output folder** as the source, or to `/mnt/user-data/outputs/` if no writable folder is available.

**File naming convention:**
```
BRD_<ProjectName>.md
PRD_<ProjectName>.md
TDD_<ProjectName>.md
DeploymentPlan_<ProjectName>.md
ReleaseNotes_<ProjectName>.md
ADR_<DecisionTitle>_<ProjectName>.md
```

For each document, read the corresponding template from the `references/` folder before generating:
- `references/brd-template.md`
- `references/prd-template.md`
- `references/tdd-template.md`
- `references/deployment-plan-template.md`
- `references/release-notes-template.md`
- `references/adr-template.md`

---

### Phase 4 — Review & Iteration

After generating all documents:
1. Present the files to the user using `present_files`
2. Ask: *"Would you like to refine any section or add more detail to a specific document?"*
3. Apply changes and re-present updated files

---

## Key Principles

- **Never fabricate** critical details like version numbers, dates, stakeholder names, or technical decisions — ask if missing
- **Always note assumptions** made in an `> ℹ️ Assumption:` callout block inline in the document
- **Keep language consistent** with the source material (match formality level)
- **BRD uses business language** — avoid technical jargon
- **TDD and ADR use technical language** — be precise and specific
- **Release Notes are concise** — use bullet points, avoid paragraphs
- For ADR, generate **one ADR file per architectural decision** identified

---

## Document Selection

If the user has not specified which documents they want, ask:

> *"Which documents would you like me to generate?"*
> - BRD
> - PRD
> - TDD
> - Deployment Plan
> - Release Notes
> - ADR
> - All of the above

Default to **All** if the user says "all project docs" or similar.
