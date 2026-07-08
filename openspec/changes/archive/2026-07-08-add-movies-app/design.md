## Context

The Movies project is a fresh Django 4.2 scaffold with no apps, models, or business logic. The project's `AGENTS.md` establishes conventions for app structure (services.py, selectors.py, thin tasks) but no code exists yet. This change creates the first app (`apps/movies`) and lays the data foundation.

## Goals / Non-Goals

**Goals:**
- Create the `apps/movies` Django app following project conventions
- Define a custom User model (email-based, extending `AbstractUser`)
- Define Movie, Showtime, and Reservation models with appropriate fields
- Implement `__str__()` on all models for admin readability
- Register the app in `INSTALLED_APPS`
- Generate initial migration

**Non-Goals:**
- Admin configuration (registering models in admin.py) — deferred to a future change
- API endpoints (DRF serializers/views) — out of scope
- Business logic services — will be added when workflows are needed
- Permissions or role-based access — deferred to `apps/accounts`

## Decisions

1. **App location: `apps/movies`** — The project uses `apps/` prefix convention (per AGENTS.md). Rather than putting movies at the root, placing it under `apps/` keeps the pattern consistent for future apps like `apps/orders`, `apps/accounts`.

2. **Custom User model with email auth** — Django's default User uses username; for this domain, email-based login is more natural. The model extends `AbstractUser` with `username = None` and `email` set to `unique=True, email_field=True`. This is a critical early decision because changing the user model after migrations is painful.

3. **`AutoField` vs `BigAutoField`** — Use Django's default `BigAutoField` for all primary keys. This avoids ID exhaustion issues and matches Django 4.2 defaults.

4. **CharField vs TextField for descriptions** — Movie description uses `TextField` since content length is unpredictable. Name/title fields use `CharField` with reasonable max lengths.

5. **Price storage** — Use `DecimalField` with `max_digits=6, decimal_places=2` for showtime pricing. Avoids float rounding issues for currency.

6. **Reservation status** — Use a `CharField` with choices (`confirmed`, `cancelled`) rather than a boolean. Allows future statuses (e.g., `pending`, `refunded`) without schema changes.

7. **No `related_name` on FK fields** — Use Django's default `_set` naming for now. `related_name` can be added later if query readability becomes an issue.

## Risks / Trade-offs

- **[Risk] Custom User model is irreversible after first migration** → Mitigation: Create it in the initial migration of this change. No data exists yet so there is no migration cost.
- **[Risk] `apps/` directory doesn't exist yet** → Mitigation: First step in tasks is creating the directory and `__init__.py`.
- **[Trade-off] No soft-delete or audit fields** → Keeping models simple for now. `created_at`/`updated_at` can be added later via a future migration.
- **[Risk] Seat availability race conditions** → Not addressed in this change (no booking logic yet). Future `services.py` should use `select_for_update()` when confirming reservations.
