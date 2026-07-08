## Context

The `apps/movies` app has a fully defined data model (Movie, Showtime, Reservation, User) but no views or URLs. Currently only `admin/` is routed. The app lacks templates, app-level URL configuration, and any browser-facing entry points. This design covers the first set of view functions to create an interactive surface.

## Goals / Non-Goals

**Goals:**
- Home page view at `/` rendering a simple welcome template
- Movie listing view at `/movies/` displaying all movies from the database
- Reservation flow at `/reserve/<showtime_id>/` that creates a Reservation with hard-coded values (first user, 1 seat) and redirects
- Confirmation redirect target at `/reservation/<id>/`
- App-level `urls.py` included from project root
- Basic templates for each view
- Documentation of all URL endpoints, arguments, and return types

**Non-Goals:**
- User authentication or session management
- Form validation or user input handling (hard-coded values per spec)
- Styling or frontend framework integration
- REST API endpoints (DRF not involved)
- Permission checks or role-based access

## Decisions

- **Function-based views** over class-based views: The views are simple enough that FBVs keep the code minimal and readable. No shared behavior or mixins are needed at this stage.
- **Hard-coded reservation values**: The spec explicitly asks for hard-coded values (first user in DB, 1 seat). This avoids form handling complexity in the initial implementation.
- **Separate template per view**: Each view gets its own template under `apps/movies/templates/movies/` for clarity, even though some could share a base layout.
- **Redirect after reservation**: Uses Django's `redirect()` to send the user to the confirmation page, following the Post/Redirect/Get pattern.
- **No services.py layer**: At this stage the views call the ORM directly. A service layer can be extracted later if reservation logic grows.

## Risks / Trade-offs

- Hard-coded user lookup (`User.objects.first()`) will fail if no users exist → Mitigation: the view checks and returns a fallback response if the user table is empty.
- No error handling for missing showtime or reservation → Mitigation: use `get_object_or_404` for graceful 404 responses.
- Templates are minimal HTML with no base template → Trade-off accepted for initial simplicity; a base template can be added later.
