## Context

The home page template at `apps/movies/templates/movies/home.html` is a static HTML page that currently only links to the movie listing. Login, registration, and search pages exist (with URL names `login`, `register`, `movie-search`) but are not linked from the home page.

## Goals / Non-Goals

**Goals:**
- Add navigation links to login, register, and search on the home page
- Use existing Django `{% url %}` template tags to reference named URL patterns
- Preserve the existing "Browse Movies" link and page layout

**Non-Goals:**
- No changes to backend views, URL patterns, or models
- No styling or layout overhaul — just add links to the existing template
- No authentication state awareness (e.g., showing login vs logout) — that is future work

## Decisions

No architectural decisions required. This is a straightforward template edit using established patterns — the codebase already uses `{% url %}` tags for navigation (`login.html`, `register.html`, `list.html`, etc.).

## Risks / Trade-offs

- [Low] Links will always appear regardless of authentication state — users will see "Login" even when logged in. Acceptable for scope; auth-aware nav can be added later.
