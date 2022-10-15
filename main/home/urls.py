from django.urls import path
from main.home import views

app_name = "home"

urlpatterns = [
    path(
        route="",
        view=views.HomeView.as_view(),
        name="home_list_view",
    ),

]
