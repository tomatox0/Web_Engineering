# user-accounts

## ADDED Requirements

### Requirement: User roles and permissions documented

The user accounts module SHALL support role-based access control for customers and staff.

#### Scenario: Permission checks in views
- **WHEN** an agent adds permission checks to views or API endpoints
- **THEN** the checks MUST be defined in `apps/accounts`
- **THEN** both web views and API endpoints MUST be updated when permissions change

#### Scenario: Permission change tests
- **WHEN** an agent modifies permission logic
- **THEN** tests MUST be added for the changed permissions

### Requirement: Role-based access enforced

The system SHALL enforce role-based access for staff-facing features.

#### Scenario: Staff role separation
- **WHEN** a staff user accesses admin features
- **THEN** the system MUST verify the user has the required role
- **THEN** unauthorized access MUST be denied with an appropriate response
