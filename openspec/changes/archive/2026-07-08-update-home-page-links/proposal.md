## Why

The home page currently only links to the movie listing, making login, registration, and search hard to discover. New visitors have no obvious way to sign up or log in, and returning users cannot search movies from the landing page.

## What Changes

- Add a **login link** (`{% url 'login' %}`) to the home page template
- Add a **register link** (`{% url 'register' %}`) to the home page template
- Add a **search link** (`{% url 'movie-search' %}`) to the home page template
- No changes to views, URLs, models, or any backend code

## Capabilities

### New Capabilities

None. No new capabilities are introduced — this is strictly a template navigation change.

### Modified Capabilities

None. No spec-level requirements are changing. The existing `movie-views` spec already covers the home page view; the template content is an implementation detail.

## Impact

- **File changed:** `apps/movies/templates/movies/home.html` only
- **No backend, URL, or model changes**
- **No new dependencies**
