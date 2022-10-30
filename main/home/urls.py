from django.urls import path

from main.home import views

app_name = "home"

urlpatterns = [
    path("login", views.UserLoginView.as_view(), name="login"),
    path(
        route="",
        view=views.HomeView.as_view(),
        name="home_list_view",
    ),
    path(
        route="profile",
        view=views.ProfileView.as_view(),
        name="profile_list_view",
    ),
]
