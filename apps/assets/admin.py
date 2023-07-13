from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model

from apps.core.models import ProjectModel, ProjectUsersRelation

# Register your models here.
from . import models


class CollectionInline(admin.StackedInline):
    model = models.CollectionModel
    extra = 0


class CollectionAdmin(admin.ModelAdmin):
    model = models.CollectionModel
    list_display = ["name"]
    # list_filter = ["is_valid"]
    search_fields = ["name"]


class BucketsInline(admin.StackedInline):
    model = models.BucketModel
    exclude = ["description"]
    extra = 0


class BucketAdmin(admin.ModelAdmin):
    model = models.BucketModel
    list_display = ["name", "protocol"]
    # list_filter = ["is_valid"]
    search_fields = ["name"]


class ObjectAdmin(admin.ModelAdmin):
    model = models.ObjectModel
    list_display = ["name", "uri"]
    # list_filter = ["is_valid"]
    search_fields = ["name"]


class ObjectsTagAdmin(admin.ModelAdmin):
    model = models.ObjectTagModel
    list_display = ["name"]
    # list_filter = ["is_valid"]
    search_fields = ["name"]


class UsersInline(admin.StackedInline):
    # model = get_user_model()
    model = ProjectUsersRelation
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    model = ProjectModel
    list_display = ["alias"]
    # list_filter = ["is_valid"]
    search_fields = ["alias"]
    inlines = [BucketsInline, UsersInline, CollectionInline]


admin.site.register(models.ProjectModel, ProjectAdmin)
admin.site.register(models.BucketModel, BucketAdmin)
admin.site.register(models.CollectionModel, CollectionAdmin)
admin.site.register(models.ObjectTagModel, ObjectsTagAdmin)
admin.site.register(models.ObjectModel, ObjectAdmin)
