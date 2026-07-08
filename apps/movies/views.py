from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, RegistrationForm, ReservationForm, SearchForm
from .models import Movie, Reservation, Showtime, User


def home(request):
    return render(request, "movies/home.html")


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movies/list.html", {"movies": movies})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegistrationForm()
    return render(request, "movies/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm()
    return render(request, "movies/login.html", {"form": form})


@login_required
def reserve(request, showtime_id):
    showtime = get_object_or_404(Showtime, pk=showtime_id)
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = Reservation.objects.create(
                user=request.user,
                showtime=showtime,
                seats=form.cleaned_data["seats"],
                status=Reservation.Status.CONFIRMED,
            )
            return redirect("reservation-confirmation", reservation_id=reservation.pk)
    else:
        form = ReservationForm()
    return render(
        request,
        "movies/reserve.html",
        {"form": form, "showtime": showtime},
    )


def movie_search(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid() and form.cleaned_data["q"]:
        q = form.cleaned_data["q"]
        results = Movie.objects.filter(
            title__icontains=q
        ) | Movie.objects.filter(description__icontains=q)
    return render(
        request, "movies/search.html", {"form": form, "results": results}
    )


def reservation_confirmation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, "movies/confirmation.html", {"reservation": reservation})
