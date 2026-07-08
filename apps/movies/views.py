from django.shortcuts import get_object_or_404, redirect, render

from .models import Movie, Reservation, Showtime, User


def home(request):
    return render(request, "movies/home.html")


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movies/list.html", {"movies": movies})


def reserve(request, showtime_id):
    showtime = get_object_or_404(Showtime, pk=showtime_id)
    user = get_object_or_404(User, pk=1)
    reservation = Reservation.objects.create(
        user=user, showtime=showtime, seats=1, status=Reservation.Status.CONFIRMED
    )
    return redirect("reservation-confirmation", reservation_id=reservation.pk)


def reservation_confirmation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, "movies/confirmation.html", {"reservation": reservation})
