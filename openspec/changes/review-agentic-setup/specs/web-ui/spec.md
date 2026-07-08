# web-ui

## ADDED Requirements

### Requirement: Staff UI as server-rendered views

The staff-facing UI SHALL use Django server-rendered views (not a separate frontend framework).

#### Scenario: View convention
- **WHEN** an agent creates a staff-facing page
- **THEN** the view MUST be in `apps/web/views.py`
- **THEN** templates MUST use Django template language

### Requirement: Navigation and URL naming consistent

Web UI URLs SHALL follow consistent naming conventions.

#### Scenario: URL names stable
- **WHEN** an agent defines web UI URLs
- **THEN** URL names MUST NOT be renamed unless explicitly asked
- **THEN** URL patterns MUST be defined in `apps/web/urls.py`
