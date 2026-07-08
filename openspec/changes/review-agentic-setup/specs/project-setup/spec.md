# project-setup

## ADDED Requirements

### Requirement: Project configuration documented

The project SHALL document its tech stack, dependencies, and development setup in the openspec config and AGENTS.md.

#### Scenario: Config populated
- **WHEN** an agent reads `openspec/config.yaml`
- **THEN** the config SHALL contain a `context` field with tech stack (Python, Django, DRF, Celery)
- **THEN** the config SHALL contain artifact-specific rules for proposal, design, specs, and tasks

#### Scenario: AGENTS.md reflects current state
- **WHEN** an agent reads `AGENTS.md`
- **THEN** it SHALL accurately describe the project's current state (not aspirational apps that don't exist yet)
- **THEN** it SHALL link to relevant capability specs for detailed guidance

### Requirement: opencode commands for common workflows

The project SHALL provide opencode commands for the most common development workflows.

#### Scenario: Server command available
- **WHEN** an agent needs to start the development server
- **THEN** there SHALL be a command or documented instruction to run `python manage.py runserver`

#### Scenario: Test command available
- **WHEN** an agent needs to run tests
- **THEN** there SHALL be a command or documented instruction to run `pytest`

#### Scenario: Migration commands available
- **WHEN** an agent needs to create or apply migrations
- **THEN** there SHALL be commands for `python manage.py makemigrations` and `python manage.py migrate`

### Requirement: Conventions documented

The project SHALL document its coding conventions for service/selector layers, Celery tasks, and testing.

#### Scenario: Service layer convention
- **WHEN** an agent creates business workflow logic
- **THEN** it MUST place it in `services.py`, not in views or serializers

#### Scenario: Selector convention
- **WHEN** an agent creates reusable query logic
- **THEN** it MUST place it in `selectors.py`

#### Scenario: Celery task convention
- **WHEN** an agent creates a Celery task
- **THEN** the task MUST be thin and delegate to a service function

#### Scenario: Testing expectations
- **WHEN** an agent modifies order status changes, permission changes, or API response shapes
- **THEN** it MUST add or update corresponding tests
