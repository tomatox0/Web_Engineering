## Why

The project currently has no form handling or user input validation. The `reserve` view uses hardcoded values (pk=1, seats=1), and there are no registration, login, or search capabilities. This limits the app to demo-only functionality.

## What Changes

- Create Django Forms for User Registration (POST), Login (POST), and Reservation (POST)
- Create a Search form for movies using GET
- Update the `reserve` view to accept user input via a form instead of hardcoded values
- Add a new `search` view and URL pattern for movie search
- Add new URL patterns for registration and login
- Render all forms with basic Django templates
- Add proper CSRF protection and form validation via `is_valid()`
- Update the `movie-views` spec to reflect reservation form changes (replacing hardcoded values)

## Capabilities

### New Capabilities

- `user-forms`: User Registration form (email, password, name) and Login form (email, password) with validation, CSRF protection, and template rendering
- `movie-search`: Movie search via GET form with query parameter, filtering Movie objects by title/description, and result display

### Modified Capabilities

- `movie-views`: The reserve view will be updated from hardcoded values to use a Django Form for seat selection and user assignment

## Impact

- `apps/movies/forms.py` (new file): All form classes
- `apps/movies/views.py`: Updated `reserve` view, new `register`, `login`, `movie_search` views
- `apps/movies/urls.py`: New URL patterns for register, login, search
- `apps/movies/templates/movies/`: New templates for register, login, search forms
- `openspec/specs/movie-views/spec.md`: Updated Requirement: Reservation processing to reflect form-based input
