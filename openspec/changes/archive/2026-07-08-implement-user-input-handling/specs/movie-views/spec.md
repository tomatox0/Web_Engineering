## MODIFIED Requirements

### Requirement: Reservation processing

The system SHALL accept a POST request at `/reserve/<showtime_id>/` that validates user-provided seat count via a Django Form, associates the reservation with the authenticated user, and redirects to the confirmation page.

#### Scenario: Reservation created with form input

- **WHEN** a user is authenticated and submits a valid seat count via POST to `/reserve/1/`
- **THEN** the system creates a Reservation record with the submitted seat count, status "confirmed", associated with the authenticated user, and redirects to `/reservation/<new_reservation_id>/`

#### Scenario: Invalid seat count

- **WHEN** a user submits a seat count of 0 or a negative number
- **THEN** the system returns the reservation form with a seat validation error

#### Scenario: Showtime not found

- **WHEN** a user submits to `/reserve/999/` and no Showtime with id=999 exists
- **THEN** the system returns HTTP 404

#### Scenario: Unauthenticated user

- **WHEN** an unauthenticated user submits to `/reserve/1/`
- **THEN** the system returns the reservation form with an authentication error or prompts login

#### Scenario: Reservation form renders

- **WHEN** a GET request is made to `/reserve/1/` by an authenticated user
- **THEN** the system returns HTTP 200 and renders `movies/reserve.html` with a form containing a seat count field
