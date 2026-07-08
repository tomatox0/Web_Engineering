from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.movie.title} at {self.start_time}"


class Reservation(models.Model):
    class Status(models.TextChoices):
        CONFIRMED = "confirmed", "Confirmed"
        CANCELLED = "cancelled", "Cancelled"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.CONFIRMED,
    )

    def __str__(self):
        return f"{self.user.email} - {self.showtime.movie.title} at {self.showtime.start_time} ({self.status})"
