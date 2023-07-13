from django.contrib import admin

# Register your models here.
from . import models


class RepositoryAdmin(admin.ModelAdmin):
    model = models.RepositoryModel
    list_display = ["name", "uri"]
    # list_filter = ["is_valid"]
    search_fields = ["name"]


admin.site.register(models.RepositoryModel, RepositoryAdmin)
