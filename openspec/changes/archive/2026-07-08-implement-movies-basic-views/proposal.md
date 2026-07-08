## Why

The `apps/movies` app has models (Movie, Showtime, Reservation, User) defined but no way for users to interact with them via the browser. Basic view functions are needed to render pages, list movies, accept simple reservation requests, and navigate between pages — establishing the app's initial user-facing surface.

## What Changes

- Add a home page view that renders a welcome template
- Add a movie listing view that queries and displays all movies
- Add a reservation processing view that accepts hard-coded values and creates a Reservation record, then redirects
- Add a reservation confirmation / redirect page
- Create an app-level `urls.py` and include it from the project root URLconf
- Create basic HTML templates for each view
- Update project documentation with the URL scheme, arguments, and return values

## Capabilities

### New Capabilities
- `movie-views`: Browser-accessible view functions for the movies app, including home, movie listing, reservation processing, and redirect flows

### Modified Capabilities

<!-- No existing specs to modify; this is the first set of specs for the project. -->

## Impact

- `apps/movies/views.py` — new view functions added
- `apps/movies/urls.py` — new file created
- `apps/movies/templates/movies/` — new template files
- `the_movies/urls.py` — add `include()` for movies URLs
- `openspec/specs/movie-views/spec.md` — new spec documenting the API surface
