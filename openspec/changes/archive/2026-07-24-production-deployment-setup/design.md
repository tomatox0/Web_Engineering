## Context

The Django project (`the_movies`) is currently configured for development with SQLite and `DEBUG = True`. It uses Django's built-in development server and lacks production-ready components. The goal is to prepare for deployment on Render.com using Waitress as the WSGI server and WhiteNoise for static file serving.

Current state:
- `pyproject.toml` has only `django` as a dependency
- `settings.py` has `DEBUG = True` hardcoded, no `STATIC_ROOT`, and no WhiteNoise middleware
- No `README.md` exists with deployment instructions

## Goals / Non-Goals

**Goals:**
- Enable production deployment on Render.com
- Configure WhiteNoise for efficient static file serving
- Make DEBUG configurable via environment variable
- Provide clear deployment documentation

**Non-Goals:**
- Database migration to PostgreSQL (can be done separately)
- CI/CD pipeline setup
- Docker configuration
- SSL/TLS configuration (handled by Render.com)

## Decisions

### 1. Use Waitress as WSGI server
**Decision**: Use `waitress` as the production WSGI server.

**Rationale**: Waitress is a pure-Python WSGI server that is production-ready, cross-platform, and well-tested. It's simpler to configure than Gunicorn on Windows and works well on Render.com.

**Alternatives considered**:
- Gunicorn: More common on Linux, but Waitress is more portable and simpler for this use case
- uWSGI: More complex configuration, overkill for this project

### 2. Use WhiteNoise for static files
**Decision**: Use `whitenoise` middleware for serving static files.

**Rationale**: WhiteNoise allows Django to serve static files efficiently without requiring a separate web server (like Nginx). It compresses files, sets proper cache headers, and handles ETags.

**Alternatives considered**:
- Nginx: Requires separate server configuration, more complex on Render.com
- Django's `collectstatic` + CDN: More complex setup, overkill for this project

### 3. Environment-based DEBUG control
**Decision**: Use `os.environ.get('DEBUG', 'False')` to control DEBUG.

**Rationale**: This allows the same codebase to run in development (with DEBUG=True) and production (with DEBUG=False or not set). Render.com allows setting environment variables easily.

**Alternatives considered**:
- Hardcoded DEBUG=False: Would break development workflow
- Using `django-environ`: Adds another dependency, unnecessary for this simple case

### 4. WhiteNoise middleware placement
**Decision**: Place `WhiteNoiseMiddleware` immediately after `SecurityMiddleware`.

**Rationale**: WhiteNoise documentation recommends this placement for optimal performance. It should run early in the middleware stack to serve static files before other middleware processes the request.

## Risks / Trade-offs

### Risk: SQLite in production
**Risk**: Using SQLite in production is not recommended for production workloads.
**Mitigation**: This change prepares for production deployment but does not switch databases. Database migration to PostgreSQL can be done separately.

### Risk: Secret key in settings
**Risk**: The `SECRET_KEY` is hardcoded in settings.py.
**Mitigation**: For full production readiness, `SECRET_KEY` should also be loaded from an environment variable. This can be addressed in a follow-up change.

### Trade-off: WhiteNoise vs CDN
**Trade-off**: WhiteNoise serves static files from the Django process, which uses more memory than a CDN.
**Mitigation**: Acceptable for small to medium projects. Can migrate to CDN later if needed.

## Migration Plan

1. Add dependencies to `pyproject.toml`
2. Update `settings.py` with WhiteNoise middleware and STATIC_ROOT
3. Update `settings.py` to read DEBUG from environment
4. Create README.md with Render.com deployment instructions
5. Test locally with `waitress-serve`
6. Deploy to Render.com

**Rollback**: Remove the added dependencies and revert settings.py changes.
