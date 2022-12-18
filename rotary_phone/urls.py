from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("django.contrib.auth.urls")),  # authentication
    path("accounts/", include("django.contrib.auth.urls")),  # authentication
    path("", include("main.home.urls")),
    path("api/", include("main.api.urls")),
    path("git/", include("main.gitsvn.urls")),
    path("health/", include("main.health.urls")),
    path("system/", include("main.system.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
