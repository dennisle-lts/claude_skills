# Investment Proposal — Structure & Writing Guide

## Document Rules
- Maximum 2 pages of content
- Lead with the problem — never open with the solution
- Every section answers: "Why does this matter to the business?"
- No technical jargon — write for a non-technical executive
- End with one clear, specific ask
- Use tables for cost/benefit — executives scan, not read

---

## Output Format Example

Below is the exact Markdown structure to follow when generating `InvestmentProposal_<ProjectName>.md`.

---

```markdown
# Investment Proposal: [Project Name]

**Prepared by:** [Name, Role]
**Date:** [DD MMM YYYY]
**Presented to:** [Audience — e.g. Executive Leadership Team]
**Classification:** Confidential

---

## The Problem

[3-5 sentences making the pain real and quantifiable. Use specific examples.
Frame around business impact — time lost, money wasted, risk exposure, customer impact.]

> "[Optional: one damning sentence that captures the core cost of the current situation.]"

---

## Our Proposal

[2-3 sentences. State the solution simply — what are we building, changing, or implementing?
Do NOT go into technical detail. Focus on what changes for the business.]

---

## What the Business Gains

| Benefit | Expected Outcome |
|---------|-----------------|
| [e.g. Team Productivity] | [e.g. Reduce onboarding time from 6 weeks to 2 weeks] |
| [e.g. Deployment Reliability] | [e.g. Reduce failed deployments by 60%] |
| [e.g. Compliance Readiness] | [e.g. Audit documentation available on demand] |
| [e.g. Cost Avoidance] | [e.g. Save ~X hours/quarter in rework] |

---

## Investment Required

| Item | Estimate |
|------|----------|
| Internal team effort | [X person-days over Y weeks] |
| Tooling / software | [Cost or "No additional cost"] |
| External support | [Cost or "None required"] |
| **Total** | **[Total estimate]** |

[One sentence on payback: "Based on X hours saved per quarter, this investment is expected to pay back within [timeframe]."]

---

## What Happens If We Don't Act

- **[Risk 1]:** [Consequence — cost, missed opportunity, or growing risk]
- **[Risk 2]:** [Consequence]
- **[Risk 3]:** [Consequence]

---

## Our Recommendation

[One short paragraph restating the recommendation plainly.]

> **We are seeking [specific approval / funding amount / resource commitment] to begin [first milestone] by [date]. A decision by [date] allows us to [key benefit].**

<!-- END OF DOCUMENT -->
```

---

## Writing Tips Per Section

### The Problem
Make it specific and painful. Use numbers wherever possible — even rough estimates.
Avoid vague language like "we have inefficient processes." Say instead:
"New team members take 4-6 weeks to become productive, costing approximately X hours of senior engineer time per hire."

### Our Proposal
Two sentences maximum. "We propose to [action], which will [outcome]. This will be delivered in [timeframe] by [who]."
Resist the urge to explain HOW — that's for the SDLC docs.

### What the Business Gains
4-6 rows maximum. Every row should have a concrete, specific outcome — not "improved efficiency" but "reduce report generation time from 3 days to 2 hours."

### Investment Required
Be transparent. Hiding costs destroys credibility. Always follow the table with a payback statement.

### What Happens If We Don't Act
This is the most persuasive section. Executives respond to risk and cost of inaction more than they respond to opportunity. Keep to 3 bullets. Be honest, not alarmist.

### Our Recommendation
End with complete clarity. What decision do you need? By when? What happens next if they say yes?
