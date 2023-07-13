from django.contrib.auth.models import Group
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.assets.models import ObjectModel, BucketModel
from drf_spectacular.utils import extend_schema
from .serializers import ObjectSerializer, BucketSerializer


class ObjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = ObjectModel.objects.all().order_by("-created_at")
    serializer_class = ObjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class BucketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = BucketModel.objects.all().order_by("-created_at")
    serializer_class = BucketSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=ObjectSerializer,
    )
    @action(detail=True, methods=["post"])
    def add_object(self, request, pk=None):
        bucket: BucketModel = self.get_object()
        # serial = BucketSerializer(data=request.data)
        # print(serial)

        return Response(
            {"bucket": bucket.name, "pk": pk}, status=status.HTTP_201_CREATED
        )

    def get_queryset(self):
        return self.request.user.accounts.all()
