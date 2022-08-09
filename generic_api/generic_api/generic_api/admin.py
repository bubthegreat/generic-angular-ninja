from django.contrib import admin  # type: ignore
from .models import (
    StringConfig,
    IntConfig,
)


@admin.register(StringConfig)
class StringConfigAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "value")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


@admin.register(IntConfig)
class IntConfigAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "value")

    def __str__(self):
        return self.title
