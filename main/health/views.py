import yaml
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from main.health.forms import RuleForm
from main.health.models import DailyTracker, Rule
from main.utility.functions import LoggingService
from main.utility.mixins import JSONResponseMixin

log = LoggingService()

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)
REDIS_KEY_PREFIX = str(getattr(settings, "REDIS_KEY_PREFIX")).lower()



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
        items = dict()
        daily_tracker_today = cache.get(f'{REDIS_KEY_PREFIX}_models__daily_tracker_today')
        rules = cache.get(f'{REDIS_KEY_PREFIX}_models__rules')

        if rules is None:
            log.debug("Getting Rule data from database")
            rules = list(Rule.objects.filter(is_active=True).values("name"))
            cache.set(f'{REDIS_KEY_PREFIX}_models__rules', rules, 60 * 5)
        else:
            log.debug("Getting Rule data from cache")

        if daily_tracker_today is None:
            log.debug("Getting DailyTracker data from database")
            daily_tracker_today = DailyTracker.objects.get_daily_status()
            cache.set(f'{REDIS_KEY_PREFIX}_models__daily_tracker_today', daily_tracker_today, 60 * 5)
        else:
            log.debug("Getting DailyTracker data from cache")

        context["rules"] = rules
        context["daily_tracker"] = daily_tracker_today
        context["items"] = items

        return self.render_to_json_response(context, **response_kwargs)
