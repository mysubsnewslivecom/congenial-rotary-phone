from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from main.api import (
    views,
    views_gitsvn,
    views_health,
    views_home,
    views_movieflex,
    views_tasks,
)

app_name = "api"

# newly registered ViewSet
router = routers.DefaultRouter()
router.register(r"project", viewset=views_gitsvn.ProjectDetailAPI, basename="project")
router.register(r"health/rule", viewset=views_health.RuleAPI, basename="rule")
router.register(r"health/dt", viewset=views_health.DailyActivityViewset, basename="dt")
router.register(
    r"trigger/health/daily",
    viewset=views_health.TriggerHealth,
    basename="trigger-health",
)
router.register(
    r"movieflex/movie", viewset=views_movieflex.MediaViewset, basename="movie"
)
router.register(
    r"movieflex/watching", viewset=views_movieflex.WatchingViewset, basename="watching"
)
router.register(r"celery/tasks", viewset=views.TaskResultViewset, basename="tasks")
router.register(r"tasks/todo", viewset=views_tasks.TodoViewset, basename="todo")
router.register(r"movieflex/anime", viewset=views_movieflex.WebScrappingViewset, basename="movieflex-anime")
router.register(r"home/epl", viewset=views_home.EPLListing, basename="home-epl")


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
    path(
        route="ip",
        view=views_home.IpifyAPI.as_view(),
        name="ipify_list_view",
    ),
]
