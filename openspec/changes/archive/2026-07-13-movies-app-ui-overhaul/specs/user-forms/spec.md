## MODIFIED Requirements

### Requirement: User registration form
The system SHALL provide a registration page at `/register/` that accepts user-provided email, password (with confirmation), first name, and last name via form inputs with explicit `<label>` elements and `id`/`for` bindings, validates the input, creates a new `movies.User` record, and redirects to the home page upon success.

#### Scenario: Successful registration
- **WHEN** a user submits valid registration data (email, matching passwords, first name, last name) via POST to `/register/`
- **THEN** the system creates a new `movies.User` record, logs the user in, and redirects to `/`

#### Scenario: Duplicate email registration
- **WHEN** a user submits a registration with an email that already exists
- **THEN** the system returns the registration form with an email validation error

#### Scenario: Password mismatch
- **WHEN** a user submits a registration where password and confirmation do not match
- **THEN** the system returns the registration form with a password validation error

#### Scenario: Registration form renders
- **WHEN** a user navigates to `/register/` via GET
- **THEN** the system returns HTTP 200 and renders `movies/register.html` with a blank registration form where each input has a visible `<label>` element

### Requirement: Login form
The system SHALL provide a login page at `/login/` that accepts email and password via form inputs with explicit `<label>` elements and `id`/`for` bindings, authenticates against `django.contrib.auth`, and redirects to the home page upon success.

#### Scenario: Successful login
- **WHEN** a user submits valid credentials via POST to `/login/`
- **THEN** the system authenticates the user, creates a session, and redirects to `/`

#### Scenario: Invalid credentials
- **WHEN** a user submits invalid credentials via POST to `/login/`
- **THEN** the system returns the login form with a generic authentication error message

#### Scenario: Login form renders
- **WHEN** a user navigates to `/login/` via GET
- **THEN** the system returns HTTP 200 and renders `movies/login.html` with a blank login form where each input has a visible `<label>` element
