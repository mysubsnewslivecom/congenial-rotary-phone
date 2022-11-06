import yaml
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from main.health.forms import RuleForm
from main.health.models import DailyTracker, Rule
from main.utility.mixins import JSONResponseMixin


class HealthHomeView(TemplateView):
    template_name = "health.html"
    form_class = RuleForm
    model = Rule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        return context


class RuleCreateView(CreateView):
    model = Rule
    form_class = RuleForm
    success_url = reverse_lazy("health:health_list_view")
    success_message = "Rule added!"


class JSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        context = dict()
        # rules = list(Rule.objects.values("name","id", "is_active",))
        rules = list(Rule.objects.values())
        dt = list(DailyTracker.objects.values())
        context["rules"] = rules
        context["daily_tracker"] = dt
        print(
            yaml.dump(
                context,
            )
        )
        return self.render_to_json_response(context, **response_kwargs)
