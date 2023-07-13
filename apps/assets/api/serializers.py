from django.contrib.auth.models import Group
from apps.accounts.models import CustomUser
from rest_framework import serializers
from apps.assets import models

# from django.contrib.auth import get_user_model


# User = get_user_model()
class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CollectionModel
        fields = ["name", "description"]


class ObjectSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(
        source="owner.username",
    )
    # collection = CollectionSerializer(many=True, read_only=True)
    collection = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="uid"
    )

    class Meta:
        model = models.ObjectModel
        fields = [
            "name",
            "owner",
            "uri",
            "description",
            "content_type",
            "file_format_type",
            "collection",
        ]


class BucketSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(
        source="owner.username",
    )
    # collection = CollectionSerializer(many=True, read_only=True)
    # collection = serializers.SlugRelatedField(
    #    many=True, read_only=True, slug_field="collectionid"
    # )

    class Meta:
        model = models.BucketModel
        fields = [
            "name",
            "uri",
            "protocol",
            "description",
            "owner",
        ]
