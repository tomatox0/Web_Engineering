## 1. Dependencies

- [x] 1.1 Add `waitress` and `whitenoise` to `pyproject.toml` dependencies

## 2. Django Settings Configuration

- [x] 2.1 Add `import os` to settings.py
- [x] 2.2 Add `whitenoise.middleware.WhiteNoiseMiddleware` after `SecurityMiddleware` in MIDDLEWARE
- [x] 2.3 Add `STATIC_ROOT = BASE_DIR / "staticfiles"` to settings.py
- [x] 2.4 Update `DEBUG` to read from environment variable: `DEBUG = os.environ.get("DEBUG", "False") == "True"`

## 3. Documentation

- [x] 3.1 Create README.md with project overview
- [x] 3.2 Add Render.com deployment instructions (environment variables, build command, start command)
- [x] 3.3 Add local development instructions
- [x] 3.4 Add production testing instructions (waitress-serve)

## 4. Verification

- [x] 4.1 Run `python manage.py collectstatic` to verify STATIC_ROOT configuration
- [x] 4.2 Test locally with `waitress-serve --listen=0.0.0.0:8080 the_movies.wsgi:application`
