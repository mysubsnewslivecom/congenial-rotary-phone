from django.urls import path

from main.system import views

app_name = "system"

urlpatterns = [
    path("", views.SystemHomeView.as_view(), name="system_home"),
]
