## ADDED Requirements

### Requirement: Production dependencies
The project SHALL include `waitress` and `whitenoise` as production dependencies.

#### Scenario: Dependencies are present
- **WHEN** the project is installed with production dependencies
- **THEN** `waitress` and `whitenoise` packages are available

### Requirement: WhiteNoise middleware configuration
The Django settings SHALL configure `whitenoise.middleware.WhiteNoiseMiddleware` immediately after `SecurityMiddleware`.

#### Scenario: Middleware order
- **WHEN** Django processes a request
- **THEN** `WhiteNoiseMiddleware` runs directly after `SecurityMiddleware`

### Requirement: Static files configuration
The Django settings SHALL set `STATIC_ROOT` to enable static file collection.

#### Scenario: Static root is configured
- **WHEN** `collectstatic` is run
- **THEN** static files are collected to the configured `STATIC_ROOT` directory

### Requirement: Environment-based debug control
The Django settings SHALL allow `DEBUG` to be controlled via the `DEBUG` environment variable, defaulting to `False` in production.

#### Scenario: Debug via environment variable
- **WHEN** the `DEBUG` environment variable is set to `"True"`
- **THEN** `DEBUG` is `True`

#### Scenario: Debug defaults to false
- **WHEN** the `DEBUG` environment variable is not set
- **THEN** `DEBUG` is `False`

### Requirement: Deployment documentation
The project SHALL include a README.md with step-by-step deployment instructions for Render.com using Waitress.

#### Scenario: Render.com instructions exist
- **WHEN** a developer reads the README.md
- **THEN** they find complete deployment steps for Render.com including environment variable setup, build commands, and start commands
