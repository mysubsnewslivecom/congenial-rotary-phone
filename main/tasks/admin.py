from django.contrib import admin

from main.tasks.models import Todo

admin.site.register(Todo)
