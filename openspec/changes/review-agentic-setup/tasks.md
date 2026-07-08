## 1. Config & Project Context

- [ ] 1.1 Populate `openspec/config.yaml` with project context: tech stack (Python 3.9+, Django 4.2+, DRF, Celery), domain (order management and staff workflows), and artifact-specific rules for proposal, design, specs, and tasks
- [ ] 1.2 Create `.opencode.json` at project root with project-aware settings (commands reference, agent guidelines pointer)

## 2. AGENTS.md Rewrite

- [ ] 2.1 Rewrite `AGENTS.md` to accurately reflect the current project state (skeleton Django project with planned apps, not existing apps)
- [ ] 2.2 Add references from AGENTS.md to capability specs in `openspec/specs/` for detailed guidance

## 3. Main Specs

- [ ] 3.1 Create `openspec/specs/project-setup/spec.md` (sync from change delta spec) — project conventions, configuration, commands
- [ ] 3.2 Create `openspec/specs/order-management/spec.md` (sync from change delta spec) — order lifecycle, services/selectors conventions
- [ ] 3.3 Create `openspec/specs/user-accounts/spec.md` (sync from change delta spec) — roles, permissions, access control
- [ ] 3.4 Create `openspec/specs/api-layer/spec.md` (sync from change delta spec) — DRF API versioning, response shape stability
- [ ] 3.5 Create `openspec/specs/web-ui/spec.md` (sync from change delta spec) — server-rendered views, URL naming

## 4. opencode Commands

- [ ] 4.1 Create or update opencode commands for common Django workflows: runserver, pytest, makemigrations, migrate
- [ ] 4.2 Verify commands are discoverable via opencode CLI

## 5. Verification

- [ ] 5.1 Read all artifacts (AGENTS.md, config.yaml, specs) and verify internal consistency — no contradictions between files
- [ ] 5.2 Run a dry-run `openspec validate` or manual review to confirm the agentic setup is coherent
