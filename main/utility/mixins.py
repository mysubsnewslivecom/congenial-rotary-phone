import uuid

from django.db import models
from django.http import JsonResponse

from main.utility.functions import LoggingService

log = LoggingService()


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at",
        help_text="Created Timestamp",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at",
        help_text="Updated Timestamp",
    )

    class Meta:
        """Setting up the abstract model class"""

        abstract = True


class ActiveStatusMixin(models.Model):
    is_active = models.BooleanField(
        default=True, verbose_name="Is active", help_text="is active"
    )

    class Meta:
        """Setting up the abstract model class"""

        abstract = True


class PrimaryIdMixin(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        """Setting up the abstract model class"""

        abstract = True


class UUIDMixin(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        """Setting up the abstract model class"""

        abstract = True


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """

        return context
