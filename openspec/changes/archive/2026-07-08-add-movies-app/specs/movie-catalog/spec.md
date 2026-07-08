## ADDED Requirements

### Requirement: Movie management
The system SHALL store movies with a title, description, release date, and duration.

#### Scenario: Create a movie
- **WHEN** a movie is created with title, description, release date, and duration
- **THEN** the movie SHALL be persisted and retrievable by ID

#### Scenario: String representation
- **WHEN** a movie object is rendered as a string
- **THEN** it SHALL return the movie title via `__str__()`

### Requirement: Showtime scheduling
The system SHALL associate showtimes with a movie, screening time, and ticket price.

#### Scenario: Create showtime for a movie
- **WHEN** a showtime is created linked to an existing movie
- **THEN** the showtime SHALL record the screening datetime and ticket price

#### Scenario: Showtime string representation
- **WHEN** a showtime object is rendered as a string
- **THEN** it SHALL show the movie title and screening datetime via `__str__()`

#### Scenario: Showtime belongs to a movie
- **WHEN** querying a showtime's movie
- **THEN** the related movie SHALL be accessible via a ForeignKey relationship

### Requirement: Price storage
The system SHALL store ticket prices as decimal values with 2 decimal places.

#### Scenario: Price precision
- **WHEN** a price of 12.50 is set on a showtime
- **THEN** the stored value SHALL be exactly 12.50 with no floating-point rounding errors
