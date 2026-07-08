## 1. Project Setup

- [x] 1.1 Create `apps/` directory with `__init__.py`
- [x] 1.2 Create `apps/movies` Django app (via `manage.py startapp movies apps/movies` or manually)
- [x] 1.3 Add `apps.movies` to `INSTALLED_APPS` in `the_movies/settings.py`
- [x] 1.4 Set `AUTH_USER_MODEL = "movies.User"` in settings

## 2. User Model

- [x] 2.1 Define `User` model in `apps/movies/models.py` extending `AbstractUser` with `username = None` and `email` as the unique identifier (`USERNAME_FIELD = "email"`)
- [x] 2.2 Set `REQUIRED_FIELDS = []` on the User model
- [x] 2.3 Implement `__str__()` on User returning the user's email

## 3. Movie Model

- [x] 3.1 Define `Movie` model with fields: `title` (CharField), `description` (TextField), `release_date` (DateField), `duration` (PositiveIntegerField for minutes)
- [x] 3.2 Implement `__str__()` on Movie returning the title

## 4. Showtime Model

- [x] 4.1 Define `Showtime` model with fields: `movie` (ForeignKey to Movie), `start_time` (DateTimeField), `price` (DecimalField max_digits=6 decimal_places=2)
- [x] 4.2 Implement `__str__()` on Showtime returning movie title and screening datetime

## 5. Reservation Model

- [x] 5.1 Define `Reservation` model with fields: `user` (ForeignKey to User), `showtime` (ForeignKey to Showtime), `seats` (PositiveIntegerField default=1), `status` (CharField with choices: confirmed/cancelled, default="confirmed")
- [x] 5.2 Implement `__str__()` on Reservation returning user email, movie title, and screening datetime

## 6. Migrations

- [x] 6.1 Generate initial migration for the movies app (`manage.py makemigrations movies`)
- [x] 6.2 Apply migrations (`manage.py migrate`)

## 7. Verification

- [x] 7.1 Verify models create correctly via Django shell or test
- [x] 7.2 Verify `__str__()` returns expected values on all models
- [x] 7.3 Run `pytest` to ensure no test failures
