from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("movies/", views.movie_list, name="movie-list"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("search/", views.movie_search, name="movie-search"),
    path("reserve/<int:showtime_id>/", views.reserve, name="reserve"),
    path(
        "reservation/<int:reservation_id>/",
        views.reservation_confirmation,
        name="reservation-confirmation",
    ),
]
