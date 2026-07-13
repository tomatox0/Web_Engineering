## MODIFIED Requirements

### Requirement: Home page
The system SHALL render a welcome page at the root URL (`/`) using a Django template with semantic HTML structure, a `<header>` containing site title and navigation, a `<main>` section with the welcome content, and a `<footer>`.

#### Scenario: Home page renders successfully
- **WHEN** a user navigates to `/`
- **THEN** the system returns HTTP 200 and renders `movies/home.html` containing `<header>`, `<nav>`, `<main>`, and `<footer>` semantic elements

### Requirement: Movie listing
The system SHALL display a list of all movies at `/movies/`, showing title, description, release date, and duration for each movie. The page SHALL use semantic HTML with `<article>` elements for each movie entry inside a `<main>` section.

#### Scenario: Movies are listed
- **WHEN** a user navigates to `/movies/`
- **THEN** the system returns HTTP 200 and renders `movies/list.html` containing all Movie records inside semantic HTML elements

#### Scenario: No movies exist
- **WHEN** a user navigates to `/movies/` and no Movie records exist
- **THEN** the system returns HTTP 200 and renders an empty list message inside a `<main>` element

### Requirement: Reservation processing
The system SHALL accept a POST request at `/reserve/<showtime_id>/` that validates user-provided seat count via a Django Form with explicit `<label>` elements for each input, associates the reservation with the authenticated user, and redirects to the confirmation page.

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
- **THEN** the system returns HTTP 200 and renders `movies/reserve.html` with a form containing a seat count field with an explicit `<label>` element

### Requirement: Reservation confirmation page
The system SHALL display a confirmation page at `/reservation/<id>/` showing the reservation details (user email, movie title, showtime, seats, status) inside semantic HTML structure.

#### Scenario: Confirmation page renders
- **WHEN** a user navigates to `/reservation/1/` and a Reservation with id=1 exists
- **THEN** the system returns HTTP 200 and renders `movies/confirmation.html` with the reservation details inside a `<main>` element

#### Scenario: Reservation not found
- **WHEN** a user navigates to `/reservation/999/` and no Reservation with id=999 exists
- **THEN** the system returns HTTP 404
