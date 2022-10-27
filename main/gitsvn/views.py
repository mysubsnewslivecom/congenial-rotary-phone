from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from main.gitsvn.models import ProjectDetail


class GitHomeView(LoginRequiredMixin, TemplateView):
    template_name = "gitsvn.html"

    def get_queryset(self):
        queryset = ProjectDetail.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query_set"] = self.get_queryset()
        print(self.request.user)
        return context


class GitProjectDetail(LoginRequiredMixin, DetailView):
    model = ProjectDetail
