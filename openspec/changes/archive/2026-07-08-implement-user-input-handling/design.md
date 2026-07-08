## Context

The movies app has 4 basic function-based views with no form handling. The `reserve` view hardcodes user pk=1 and seat count=1. There is no user registration, login, or movie search. All input so far comes only from URL path parameters.

## Goals / Non-Goals

**Goals:**
- Replace hardcoded values in `reserve` with a Django Form for seat selection
- Add User Registration form (email, password1, password2, first_name, last_name) creating `movies.User` instances
- Add Login form (email, password) using Django's `authenticate()` and `login()`
- Add Movie Search via GET form filtering by title/description
- Keep function-based views for consistency with existing code
- Add templates for each new form
- Add URL patterns for new views

**Non-Goals:**
- Password reset / email verification flows
- User profile editing
- API endpoints (REST) for these forms
- Pagination of search results
- AJAX/async form submission

## Decisions

- **Django Forms over manual parsing**: Using `django.forms.Form` and `ModelForm` provides built-in validation, cleaning, CSRF integration, and template rendering. Minimal boilerplate compared to manual `request.POST` parsing.
- **Function-based views**: The existing 4 views are function-based. Keeping forms in FBVs maintains consistency and avoids mixing paradigms.
- **`UserCreationForm`-style for registration**: A custom `ModelForm` for the `movies.User` model (email-based), mirroring Django's `UserCreationForm` pattern with password confirmation.
- **`authenticate()` + `login()` for auth**: Using Django's built-in auth framework since `AUTH_USER_MODEL = "movies.User"` is already configured.
- **GET form for search**: Search uses GET for bookmarkable/shareable URLs and aligns with REST conventions for read-only queries.
- **Separate template per form**: Each form gets its own template (register.html, login.html, search.html) for clarity; no base template refactoring in this change.

## Risks / Trade-offs

- **No base template**: Templates repeat boilerplate (DOCTYPE, head). This is acceptable since introducing a base template is a separate concern.
- **GET search without pagination**: For small datasets this is fine; pagination can be added later without breaking changes.
- **No rate limiting on login**: Acceptable for this phase; login brute-force protection is a future concern.
