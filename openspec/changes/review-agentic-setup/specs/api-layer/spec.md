# api-layer

## ADDED Requirements

### Requirement: DRF API endpoints versioned

The API layer SHALL use Django REST Framework and SHALL support API versioning.

#### Scenario: API response shape preserved
- **WHEN** an agent modifies an API endpoint
- **THEN** the response shape MUST NOT change without a version bump or explicit approval
- **THEN** response shape changes MUST be reflected in tests

#### Scenario: API field naming stable
- **WHEN** an agent defines or modifies API serializer fields
- **THEN** field names MUST NOT be renamed unless explicitly asked
- **THEN** serializers MUST be kept in `apps/api`

### Requirement: API test coverage

The API layer SHALL have tests for response shapes and status codes.

#### Scenario: API response change tests
- **WHEN** an agent changes API response shapes
- **THEN** tests MUST be updated or added to verify the new response format
