## Why

The project's AI-agent configuration (AGENTS.md, openspec config, opencode settings) is a generic template that doesn't reflect the actual state of the codebase. As we begin building the Django project, we need a refined agentic setup that accurately describes the project, provides useful guidance, and is synchronized between AGENTS.md, openspec specs, and opencode configuration.

## What Changes

- Rewrite AGENTS.md to accurately reflect the project's current state and conventions
- Populate `openspec/config.yaml` with project context, tech stack, and per-artifact rules
- Create initial capability specs under `openspec/specs/` for each planned Django app area
- Create or update `.opencode.json` with project-aware settings
- Add opencode commands for common project workflows
- Document conventions for service/selector layer, Celery tasks, and testing

## Capabilities

### New Capabilities
- `project-setup`: Overall project structure, Django configuration, conventions, and agentic configuration
- `order-management`: Customer order lifecycle — creation, status transitions, fulfillment
- `user-accounts`: User authentication, roles, permissions, and staff management
- `api-layer`: DRF API endpoints, serialization, versioning, and response shaping
- `web-ui`: Staff-facing server-rendered UI views, templates, and navigation

## Impact

- AGENTS.md will be rewritten — any user-local notes should be saved
- openspec/specs/ will be created from scratch
- opencode configuration may add commands/skills
- No production code is affected (pre-build phase)
