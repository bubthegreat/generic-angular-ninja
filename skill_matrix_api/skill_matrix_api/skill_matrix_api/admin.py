from django.contrib import admin  # type: ignore
from .models import (
    Employee,
    Department,
    KeyArea,
    FunctionalArea,
    Competency,
    Level,
    LevelDescription,
)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

    def __str__(self):
        return self.title


@admin.register(KeyArea)
class KeyAreaAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

    def __str__(self):
        return self.title


@admin.register(FunctionalArea)
class FunctionalAreaAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

    def __str__(self):
        return self.title


@admin.register(Competency)
class CompetencyAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

    def __str__(self):
        return self.title


@admin.register(LevelDescription)
class LevelDescriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
