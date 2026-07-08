## 1. URL Configuration

- [x] 1.1 Create `apps/movies/urls.py` with URL patterns for home, movie listing, reservation processing, and confirmation pages
- [x] 1.2 Add `include("apps.movies.urls")` to the project-level `the_movies/urls.py`

## 2. View Functions

- [x] 2.1 Add `home` view in `apps/movies/views.py` that renders `movies/home.html`
- [x] 2.2 Add `movie_list` view that queries all Movie records and renders `movies/list.html`
- [x] 2.3 Add `reserve` view that looks up a Showtime by ID, creates a Reservation with hard-coded values (first User, 1 seat, confirmed), and redirects to the confirmation page
- [x] 2.4 Add `reservation_confirmation` view that renders `movies/confirmation.html` with reservation details

## 3. Templates

- [x] 3.1 Create `apps/movies/templates/movies/home.html` with a welcome heading
- [x] 3.2 Create `apps/movies/templates/movies/list.html` that iterates over movies and displays title, description, release date, and duration
- [x] 3.3 Create `apps/movies/templates/movies/confirmation.html` showing reservation details (user email, movie title, showtime, seats, status)

## 4. Documentation

- [x] 4.1 Create `openspec/specs/movie-views/spec.md` documenting each URL endpoint, its arguments, and its return value (template rendered or redirect target)
