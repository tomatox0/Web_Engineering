## ADDED Requirements

### Requirement: Custom User Model
The system SHALL provide a custom User model that uses email for authentication instead of username.

#### Scenario: Create user with email
- **WHEN** a new user is created with an email address and password
- **THEN** the user SHALL be able to authenticate using that email and password

#### Scenario: Email uniqueness enforced
- **WHEN** a user attempts to register with an email that already exists
- **THEN** the system SHALL reject the duplicate and return a validation error

#### Scenario: Admin can view users
- **WHEN** an admin accesses the user list in the admin interface
- **THEN** each user SHALL display their email as the primary identifier via `__str__()`
