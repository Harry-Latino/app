# DRF
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.validators import UniqueValidator

# Local
from api.purchases.serializers.purchases import PurchaseLineSerializer
from apps.ecommerce.models import Purchase, PurchaseLine


class PurchaseLineView(CreateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = PurchaseLineSerializer

    def get_queryset(self):
        return PurchaseLine.objects.filter(
            purchase__user=self.request.user,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
