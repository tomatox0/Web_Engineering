## ADDED Requirements

### Requirement: Reservation creation
The system SHALL allow a user to reserve seats for a showtime.

#### Scenario: Create a reservation
- **WHEN** a user creates a reservation for a showtime with a positive number of seats
- **THEN** the reservation SHALL be persisted with status "confirmed"

#### Scenario: Reservation belongs to user and showtime
- **WHEN** querying a reservation
- **THEN** the linked user and showtime SHALL be accessible via ForeignKey relationships

#### Scenario: Reservation string representation
- **WHEN** a reservation object is rendered as a string
- **THEN** it SHALL show the user email, movie title, and screening datetime via `__str__()`

### Requirement: Reservation status tracking
The system SHALL track reservation status as "confirmed" or "cancelled".

#### Scenario: Default status is confirmed
- **WHEN** a reservation is created without specifying a status
- **THEN** its status SHALL default to "confirmed"

#### Scenario: Cancel a reservation
- **WHEN** a reservation's status is changed to "cancelled"
- **THEN** the change SHALL be persisted and retrievable

### Requirement: Seat count storage
The system SHALL store the number of reserved seats as a positive integer.

#### Scenario: Reserve multiple seats
- **WHEN** a reservation is created with 3 seats
- **THEN** the seat count SHALL be stored as 3

#### Scenario: Seat count defaults to 1
- **WHEN** a reservation is created without specifying seat count
- **THEN** the seat count SHALL default to 1
