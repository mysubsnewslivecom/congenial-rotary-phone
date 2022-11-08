from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.urls import path
from django.views.decorators.cache import cache_page

from main.health import views

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)

app_name = "health"

urlpatterns = [
    path(
        route="",
        view=cache_page(CACHE_TTL)(views.HealthHomeView.as_view()),
        name="health_list_view",
    ),
    path(
        route="rule/create",
        view=views.RuleCreateView.as_view(),
        name="rule_create_view",
    ),
    path(
        route="rule/json",
        view=views.JSONView.as_view(),
        name="rule_json_view",
    ),
]
