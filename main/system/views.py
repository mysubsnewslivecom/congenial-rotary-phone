from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class SystemHomeView(LoginRequiredMixin, TemplateView):
    template_name = "system.html"
