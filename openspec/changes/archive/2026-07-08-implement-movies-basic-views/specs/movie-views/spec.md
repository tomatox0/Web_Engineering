## ADDED Requirements

### Requirement: Home page
The system SHALL render a welcome page at the root URL (`/`) using a Django template.

#### Scenario: Home page renders successfully
- **WHEN** a user navigates to `/`
- **THEN** the system returns HTTP 200 and renders `movies/home.html`

### Requirement: Movie listing
The system SHALL display a list of all movies at `/movies/`, showing title, description, release date, and duration for each movie.

#### Scenario: Movies are listed
- **WHEN** a user navigates to `/movies/`
- **THEN** the system returns HTTP 200 and renders `movies/list.html` containing all Movie records

#### Scenario: No movies exist
- **WHEN** a user navigates to `/movies/` and no Movie records exist
- **THEN** the system returns HTTP 200 and renders an empty list message

### Requirement: Reservation processing
The system SHALL accept a POST-style request at `/reserve/<showtime_id>/` that creates a Reservation using hard-coded values (first User in the database, 1 seat, status "confirmed") and redirects to the confirmation page.

#### Scenario: Reservation created successfully
- **WHEN** a user navigates to `/reserve/1/` and a Showtime with id=1 exists
- **THEN** the system creates a Reservation record with seats=1, status="confirmed", associated with the first User, and redirects to `/reservation/<new_reservation_id>/`

#### Scenario: Showtime not found
- **WHEN** a user navigates to `/reserve/999/` and no Showtime with id=999 exists
- **THEN** the system returns HTTP 404

#### Scenario: No users exist
- **WHEN** a user navigates to `/reserve/1/` and the User table is empty
- **THEN** the system returns an appropriate error response (HTTP 404 or error page)

### Requirement: Reservation confirmation page
The system SHALL display a confirmation page at `/reservation/<id>/` showing the reservation details (user email, movie title, showtime, seats, status).

#### Scenario: Confirmation page renders
- **WHEN** a user navigates to `/reservation/1/` and a Reservation with id=1 exists
- **THEN** the system returns HTTP 200 and renders `movies/confirmation.html` with the reservation details

#### Scenario: Reservation not found
- **WHEN** a user navigates to `/reservation/999/` and no Reservation with id=999 exists
- **THEN** the system returns HTTP 404
