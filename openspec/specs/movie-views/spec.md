# Movie Views

Browser-accessible view functions for the movies app.

## URL Scheme

| URL Pattern | View Function | Arguments | Returns |
|---|---|---|---|---|
| `/` | `home` | None | Renders `movies/home.html` |
| `/movies/` | `movie_list` | None | Renders `movies/list.html` with `movies` queryset |
| `/register/` | `register` | None | GET renders `movies/register.html`; POST creates User and redirects to `/` |
| `/login/` | `login_view` | None | GET renders `movies/login.html`; POST authenticates and redirects to `/` |
| `/search/` | `movie_search` | `q` (query string, optional) | Renders `movies/search.html` with results |
| `/reserve/<int:showtime_id>/` | `reserve` | `showtime_id` (int) | GET renders `movies/reserve.html` with form; POST creates Reservation and redirects to `/reservation/<id>/` |
| `/reservation/<int:reservation_id>/` | `reservation_confirmation` | `reservation_id` (int) | Renders `movies/confirmation.html` with `reservation` object |

## Views

### Home (`/`)
Simple welcome page. No database queries. No arguments.

### Movie List (`/movies/`)
Queries all `Movie` records and passes them to the template. Shows empty state when no movies exist.

### Reserve (`/reserve/<showtime_id>/`)
Looks up `Showtime` by primary key (returns 404 if not found). On GET, renders a reservation form with seat count input. On POST, validates the seat count via `ReservationForm`, creates a `Reservation` associated with the authenticated user, and redirects to the confirmation page.

### Reservation Confirmation (`/reservation/<reservation_id>/`)
Looks up `Reservation` by primary key (returns 404 if not found). Renders details: user email, movie title, showtime time, seat count, and status.

## Requirements

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

### Requirement: Reservation confirmation page
The system SHALL display a confirmation page at `/reservation/<id>/` showing the reservation details (user email, movie title, showtime, seats, status).

#### Scenario: Confirmation page renders
- **WHEN** a user navigates to `/reservation/1/` and a Reservation with id=1 exists
- **THEN** the system returns HTTP 200 and renders `movies/confirmation.html` with the reservation details

#### Scenario: Reservation not found
- **WHEN** a user navigates to `/reservation/999/` and no Reservation with id=999 exists
- **THEN** the system returns HTTP 404
