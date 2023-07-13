import uuid
from django.db import models
from apps.accounts.models import AbstractOwned
from django.conf import settings


# Create your models here.
class BaseModel(models.Model):
    # id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField("created", auto_now_add=True)
    updated_at = models.DateTimeField("updated", auto_now=True)

    class Meta:
        abstract = True
        indexes = [models.Index(fields=["-created_at"])]


class ProjectModel(BaseModel, AbstractOwned, models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, unique=True, db_index=True, editable=False
    )
    alias: str = models.CharField(max_length=256, unique=True)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="projects",
        through="ProjectUsersRelation",
    )

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        indexes = [models.Index(fields=["alias"])]

    def __str__(self):
        return f"Prj: {self.alias}"

    def __repr__(self):
        return f"<{self.alias}>"


class ProjectUsersRelation(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)


class RepositoryModel(BaseModel, AbstractOwned, models.Model):
    name = models.CharField(max_length=256)
    uri = models.CharField(max_length=512)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(
        ProjectModel, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        # indexes = [models.Index(fields=["repo_id"])]
        verbose_name = "Repository"
        verbose_name_plural = "Repositories"

    def __str__(self):
        return f"{self.name}"
