# Deployment Plan
**Project Name:** [Project Name]
**Release Version:** [e.g., v1.2.0]
**Deployment Date:** [DD MMM YYYY]
**Prepared By:** [Name / Role]
**Environment:** [Staging | Production]

---

## 1. Overview
[Brief summary of what is being deployed and the deployment goal.]

---

## 2. Scope
[List of services, components, or databases being deployed.]
- Service 1
- Database migration scripts

---

## 3. Pre-Deployment Checklist
- [ ] Code freeze completed
- [ ] All tests passing in CI/CD
- [ ] Staging deployment verified
- [ ] Database backup taken
- [ ] Stakeholder approval obtained
- [ ] On-call team notified
- [ ] Rollback plan reviewed

---

## 4. Deployment Architecture
[Target environment and any infrastructure changes.]

| Environment | URL / Endpoint | Notes |
|-------------|---------------|-------|
| Staging | [URL] | Final UAT environment |
| Production | [URL] | Live environment |

---

## 5. Deployment Steps
| Step | Action | Owner | Est. Time |
|------|--------|-------|-----------|
| 1 | [e.g., Merge feature branch to main] | Dev Lead | 5 min |
| 2 | [e.g., Trigger CI/CD pipeline] | DevOps | 15 min |
| 3 | [e.g., Run DB migration scripts] | DevOps | 10 min |
| 4 | [e.g., Deploy to production] | DevOps | 20 min |
| 5 | [e.g., Run smoke tests] | QA | 15 min |

---

## 6. Configuration Changes
| Config | Old Value | New Value | Environment |
|--------|-----------|-----------|------------|
| [ENV_VAR] | [Old] | [New] | Production |

---

## 7. Database Migration Steps
```sql
-- Step 1: [Description]
ALTER TABLE ...;

-- Step 2: [Description]
CREATE INDEX ...;
```

---

## 8. Rollback Plan

### Trigger Conditions
[When should a rollback be initiated?]
- Critical errors in smoke tests
- Error rate exceeds [X]% post-deployment

### Rollback Steps
| Step | Action | Owner |
|------|--------|-------|
| 1 | [e.g., Re-deploy previous Docker image] | DevOps |
| 2 | [e.g., Revert DB migration] | DevOps |
| 3 | [e.g., Notify stakeholders] | PM |

---

## 9. Post-Deployment Verification
- [ ] Smoke tests passed
- [ ] Key user flows verified
- [ ] Monitoring dashboards checked
- [ ] Error rate within acceptable range
- [ ] Performance metrics normal

---

## 10. Communication Plan
| Event | Audience | Channel | Owner |
|-------|---------|---------|-------|
| Pre-deployment | Stakeholders | Email | PM |
| Deployment start | Dev team | Slack | DevOps |
| Deployment complete | All | Email/Slack | PM |
| Rollback (if needed) | Stakeholders | Email | PM |

---

## 11. Sign-off
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Manager | | | |
| Tech Lead | | | |
| QA Lead | | | |
