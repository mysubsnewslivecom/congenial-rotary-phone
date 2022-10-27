from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from main.health.forms import RuleForm
from main.health.models import Rule


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
