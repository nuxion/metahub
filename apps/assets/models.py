import uuid
from django.db import models
from apps.accounts.models import AbstractOwned
from apps.core.models import BaseModel, ProjectModel


# Create your models here.

# class CollectionTagModel(BaseModel, models.Model):
#     name = models.CharField(max_length=128)
#
#     def __str__(self):
#         return f"{self.name}"
#
#     class Meta:
#         # indexes = [models.Index(fields=["repo_id"])]
#         verbose_name = "Collection Tag"
#         verbose_name_plural = "Tags collection"


class CollectionModel(BaseModel, AbstractOwned, models.Model):
    # collectionid = models.CharField(max_length=64)
    uuid = models.UUIDField(
        default=uuid.uuid4, unique=True, db_index=True, editable=False
    )
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(
        ProjectModel, null=True, blank=True, on_delete=models.CASCADE
    )

    # tags = models.ManyToManyField(CollectionTagModel)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"
        indexes = [models.Index(fields=["name"])]


class BucketModel(BaseModel, AbstractOwned, models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, unique=True, db_index=True, editable=False
    )
    name = models.CharField(max_length=256)
    uri = models.TextField(max_length=512)
    protocol = models.CharField(max_length=16)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(
        ProjectModel, null=True, blank=True, on_delete=models.CASCADE
    )

    # tags = models.ManyToManyField(BucketTag)
    class Meta:
        verbose_name = "Bucket"
        verbose_name_plural = "Buckets"

    def __str__(self):
        return f"{self.name}"


class ObjectTagModel(BaseModel, models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        # indexes = [models.Index(fields=["repo_id"])]
        verbose_name = "Tag Object"
        verbose_name_plural = "Objects Tags"


class ObjectModel(BaseModel, AbstractOwned, models.Model):
    # oid = models.CharField(max_length=64, unique=True)
    uuid = models.UUIDField(
        default=uuid.uuid4, unique=True, db_index=True, editable=False
    )
    name = models.CharField(max_length=256)
    uri = models.CharField(max_length=256, unique=True)
    content_type = models.CharField(max_length=16, null=True, blank=True)
    file_format_type = models.CharField(max_length=16, null=True, blank=True)
    meta = models.JSONField(null=True, blank=True)
    bucket = models.ForeignKey(BucketModel, on_delete=models.CASCADE)
    collection = models.ManyToManyField(CollectionModel)
    tags = models.ManyToManyField(ObjectTagModel)

    class Meta:
        verbose_name = "Object"
        verbose_name_plural = "Objects"
        indexes = [models.Index(fields=["name"])]
