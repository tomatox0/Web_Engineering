## Context

The project has a generic opencode agent setup: AGENTS.md describes a Django order-management vision (`apps/orders`, `apps/accounts`, `apps/api`, `apps/web`) but those apps don't exist yet. The openspec config is empty, no specs exist, and no `.opencode.json` file is present. As we begin development, we need a refined agentic setup that accurately reflects the project's current state and provides useful guidance for AI agents.

## Goals / Non-Goals

**Goals:**
- Rewrite AGENTS.md to match the actual project state (minimal skeleton with a Django project plan)
- Populate `openspec/config.yaml` with project context (Python/Django, DRF, Celery)
- Create initial capability specs under `openspec/specs/` for each planned area
- Add project-aware opencode commands for common workflows (run server, tests, migrations)
- Document conventions for service/selector layers, Celery tasks, and testing

**Non-Goals:**
- Writing production code (Django models, views, URLs)
- Creating the Django apps themselves
- Setting up infrastructure (databases, queues, deployment)

## Decisions

1. **Spec-first documentation** — All canonical project knowledge lives in `openspec/specs/*.md`. AGENTS.md becomes a concise reference that points to specs for detail. This avoids duplication.
2. **One spec per bounded context** — `project-setup` covers the meta setup (config, commands, conventions). `order-management`, `user-accounts`, `api-layer`, `web-ui` each describe their domain. This matches the Django app boundaries.
3. **Delta specs in change, main specs for truth** — The change's `specs/` directory holds delta specs. During implementation, these will be synced to `openspec/specs/` (main specs). This keeps the change self-contained.
4. **Flat command structure** — opencode custom commands follow the existing `opsx-*` naming pattern for consistency.
5. **AGENTS.md as the entry point** — It stays concise (like a README for agents) with pointers to specs. The existing format is good; we just need to align content with reality.

## Risks / Trade-offs

- **[Incomplete specs]** The initial specs will be lightweight — they'll be refined as we build. Mitigation: note "initial skeleton" in each spec and update as the project grows.
- **[Stale AGENTS.md]** If we update specs but forget AGENTS.md. Mitigation: add a validation note in the tasks.
- **[Over-specification]** Too much detail up front for a project that hasn't started. Mitigation: keep specs to requirements and scenarios, not implementation.
