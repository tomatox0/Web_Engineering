## Why

The Movies project is a blank Django scaffold with no apps or models. This change establishes the foundational data layer for the core domain — users, movies, showtimes, and reservations — enabling the application to function and serve as the base for future API and admin interfaces.

## What Changes

- Create a new Django app `apps/movies`
- Register `apps.movies` in `INSTALLED_APPS`
- Define a custom User model (email-based authentication) extending `AbstractUser`
- Define Movie model with title, description, release date, duration, etc.
- Define Showtime model linking Movies to specific screening times
- Define Reservation model linking Users to Showtimes with seat count
- Implement `__str__()` on all models for admin convenience
- Generate and apply initial migrations

## Capabilities

### New Capabilities

- `user-accounts`: Custom user model, authentication, and profile fields for the Movies platform
- `movie-catalog`: Movie and Showtime models — the core catalog of films and their screening schedule
- `reservations`: Reservation model that ties users to showtimes, tracks seat count, and enforces availability

### Modified Capabilities

- *(None — no existing specs to modify.)*

## Impact

- New database tables (`movies_user`, `movies_movie`, `movies_showtime`, `movies_reservation`)
- Settings file updated with new app registration
- Initial migration created for the movies app
- Foundation laid for future API (DRF) endpoints and Django admin configuration
