# The Movies

A Django application for browsing and managing movies.

## Local Development

### Prerequisites

- Python 3.9 or higher
- pip or uv package manager

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd web-engineering
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

4. Set the DEBUG environment variable (optional, defaults to False):
   ```bash
   export DEBUG=True  # On Windows: set DEBUG=True
   ```

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Visit http://127.0.0.1:8000/ in your browser.

## Production Deployment on Render.com

### Prerequisites

- A Render.com account
- A GitHub repository with this project

### Step 1: Set Environment Variables

In your Render.com dashboard, create a new Web Service and set the following environment variables:

| Variable | Value | Description |
|----------|-------|-------------|
| `DEBUG` | `False` | Disables Django debug mode |
| `SECRET_KEY` | `<your-secret-key>` | Generate a secure secret key |
| `RENDER_EXTERNAL_HOSTNAME` | `<your-app>.onrender.com` | Your Render hostname |

### Step 2: Configure Build Settings

- **Build Command**:
  ```bash
  pip install -e . && python manage.py collectstatic --noinput
  ```

- **Start Command**:
  ```bash
  waitress-serve --listen=0.0.0.0:$PORT the_movies.wsgi:application
  ```

### Step 3: Deploy

1. Push your changes to GitHub
2. Render will automatically deploy your application
3. Visit your app's URL to verify it's working

### Environment Variables Reference

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DEBUG` | No | `False` | Set to `True` for development |
| `SECRET_KEY` | Yes | None | Django secret key for cryptographic operations |

## Production Testing (Local)

To test the production configuration locally:

1. Install production dependencies:
   ```bash
   pip install -e .
   ```

2. Set environment variables:
   ```bash
   export DEBUG=False
   export SECRET_KEY=your-secret-key
   ```

3. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

4. Run with Waitress:
   ```bash
   waitress-serve --listen=0.0.0.0:8080 the_movies.wsgi:application
   ```

5. Visit http://localhost:8080/ in your browser.

## Project Structure

```
web-engineering/
├── apps/
│   └── movies/          # Movies application
├── the_movies/          # Django project settings
│   ├── settings.py      # Configuration
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI entry point
├── pyproject.toml       # Project dependencies
└── README.md            # This file
```

## License

[Add your license here]
