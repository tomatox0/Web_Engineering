## Why

The Django project is currently configured for development only. To deploy to production (specifically Render.com), we need to add production-ready WSGI server support and static file serving. Without this, the app cannot run in production environments.

## What Changes

- Add `waitress` (production WSGI server) and `whitenoise` (static file serving) to project dependencies
- Configure `WhiteNoiseMiddleware` in Django settings for efficient static file serving
- Make `DEBUG` configurable via environment variable for production flexibility
- Set `STATIC_ROOT` for WhiteNoise to collect static files
- Add comprehensive Render.com deployment instructions to README.md

## Capabilities

### New Capabilities

- `production-deployment`: Production deployment configuration including WSGI server setup, static file serving, and platform-specific deployment documentation

### Modified Capabilities

None - no existing spec-level behavior changes.

## Impact

- **Dependencies**: `pyproject.toml` updated with `waitress` and `whitenoise`
- **Settings**: `the_movies/settings.py` updated with WhiteNoise middleware, STATIC_ROOT, and env-based DEBUG
- **Documentation**: New `README.md` with Render.com deployment guide
- **Deployment**: Enables production deployment on Render.com using Waitress WSGI server
