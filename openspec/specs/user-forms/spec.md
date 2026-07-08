# User Forms

Registration and login form handling for the movies app.

## URL Scheme

| URL Pattern | View Function | Methods | Returns |
|---|---|---|---|
| `/register/` | `register` | GET, POST | Renders `movies/register.html` or redirects to `/` |
| `/login/` | `login_view` | GET, POST | Renders `movies/login.html` or redirects to `/` |

## Requirements

### Requirement: User registration form

The system SHALL provide a registration page at `/register/` that accepts user-provided email, password (with confirmation), first name, and last name, validates the input, creates a new `movies.User` record, and redirects to the home page upon success.

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
- **THEN** the system returns HTTP 200 and renders `movies/register.html` with a blank registration form

### Requirement: Login form

The system SHALL provide a login page at `/login/` that accepts email and password, authenticates against `django.contrib.auth`, and redirects to the home page upon success.

#### Scenario: Successful login

- **WHEN** a user submits valid credentials via POST to `/login/`
- **THEN** the system authenticates the user, creates a session, and redirects to `/`

#### Scenario: Invalid credentials

- **WHEN** a user submits invalid credentials via POST to `/login/`
- **THEN** the system returns the login form with a generic authentication error message

#### Scenario: Login form renders

- **WHEN** a user navigates to `/login/` via GET
- **THEN** the system returns HTTP 200 and renders `movies/login.html` with a blank login form
