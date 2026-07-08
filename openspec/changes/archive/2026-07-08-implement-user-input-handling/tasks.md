## 1. Forms

- [x] 1.1 Create `apps/movies/forms.py` with `RegistrationForm` (ModelForm for `movies.User` with email, password1, password2, first_name, last_name; validates password match and email uniqueness)
- [x] 1.2 Add `LoginForm` (email + password fields, calls `authenticate()` in `clean()`)
- [x] 1.3 Add `ReservationForm` (seat count field with validation: minimum 1, maximum 10)
- [x] 1.4 Add `SearchForm` (query field, optional, for GET movie search)

## 2. Views

- [x] 2.1 Add `register` view in `apps/movies/views.py`: GET renders form, POST validates and creates User, logs in, redirects to home
- [x] 2.2 Add `login_view` view in `apps/movies/views.py`: GET renders login form, POST validates and logs in, redirects to home
- [x] 2.3 Update `reserve` view: require authenticated user, handle GET (render form with showtime context), handle POST (validate `ReservationForm`, create reservation), replace hardcoded user pk and seats
- [x] 2.4 Add `movie_search` view: GET reads `q` param, filters movies by title/description (icontains), renders results

## 3. URLs

- [x] 3.1 Add URL patterns for `register/`, `login/`, `search/` in `apps/movies/urls.py` with appropriate names

## 4. Templates

- [x] 4.1 Create `apps/movies/templates/movies/register.html` with registration form (CSRF, form fields, submit button, link to login)
- [x] 4.2 Create `apps/movies/templates/movies/login.html` with login form (CSRF, email/password fields, submit button, link to register)
- [x] 4.3 Create `apps/movies/templates/movies/search.html` with search form (GET, query input, submit, results list, empty state)
- [x] 4.4 Update `apps/movies/templates/movies/reserve.html` or create it: reservation form with seat count field, showing movie/showtime info

## 5. Specs & Docs

- [x] 5.1 Promote delta specs to main specs (`openspec/sync-specs` or manual copy): `user-forms/spec.md`, `movie-search/spec.md`, merged `movie-views/spec.md`
