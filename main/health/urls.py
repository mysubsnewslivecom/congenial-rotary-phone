from django.urls import path

from main.health import views

app_name = "health"

urlpatterns = [
    path(route="", view=views.HealthHomeView.as_view(), name="health_list_view"),
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
