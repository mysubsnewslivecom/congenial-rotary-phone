from django.conf import settings

from main.utility.functions import LoggingService

log = LoggingService()


def export_variables(request):
    data = dict()
    data["REDIS_LOCATION"] = settings.REDIS_LOCATION

    return data
