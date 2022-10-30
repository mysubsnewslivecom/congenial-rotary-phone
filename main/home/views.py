from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from main.home.forms import CustomUserAuthenticationForm


class UserLoginView(LoginView):
    form_class = CustomUserAuthenticationForm
    authentication_form = CustomUserAuthenticationForm

    def form_valid(self, form):
        remember_me = form.cleaned_data["remember_me"]
        login(self.request, form.get_user())

        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(LoginView, self).form_valid(form)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pending_review"] = 10
        context["open_tasks"] = 5
        context["unread_articles"] = 700
        context["budget_remaining"] = 200
        context["budget_consumed"] = "100,000.00"
        context["current_ip"] = "172.19.166.98"
        context["international_space_station"] = "-26.9884, -38.6396"
        context["temperature"] = "-26.9884"
        return context


class UserLogout(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
