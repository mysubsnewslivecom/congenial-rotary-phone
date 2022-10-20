from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# from django.conf.urls import url
from rest_framework import routers

from main.api import views

app_name = "api"

# newly registered ViewSet
router = routers.DefaultRouter()
# router.register(r"temperature", views.OpenWeatherAPI, basename="get-temperature")

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework")),
    path("schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs",
        SpectacularSwaggerView.as_view(
            # template_name="swagger-ui.html",
            url_name="api:schema"
        ),
        name="swagger-ui",
    ),
    path(
        route="weather",
        view=views.OpenWeatherAPI.as_view(),
        name="openweather_list_view",
    ),
]