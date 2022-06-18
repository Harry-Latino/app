# DRF
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    RelatedField,
)

# Local
from api.authentication.serializers.users import UserSerializer
from api.products.serializers import ProductSerializer
from apps.ecommerce.models import Purchase, PurchaseLine


class PurchaseLineSerializer(ModelSerializer):
    logged_user = SerializerMethodField(method_name="get_logged_user")
    product = ProductSerializer

    class Meta:
        model = PurchaseLine
        fields = ["id", "purchase", "product", "logged_user"]

    def get_logged_user(self, obj):
        request = self.context.get("request")
        serializer = UserSerializer(
            request.user,
            context={"request": request},
        )
        return serializer.data


class PurchaseSerializer(ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Purchase
        fields = ["id", "state", "user"]
