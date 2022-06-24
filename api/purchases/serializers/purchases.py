# DRF
from rest_framework import exceptions
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    RelatedField,
)

# Local
from rest_framework.validators import UniqueTogetherValidator

from api.authentication.serializers.users import UserSerializer
from api.products.serializers import ProductSerializer
from apps.ecommerce.models import Purchase, PurchaseLine

from apps.ecommerce.workflows import PurchaseWorkflow


class PurchaseSerializer(ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Purchase
        fields = ["id", "state", "user"]


class PurchaseLineSerializer(ModelSerializer):
    product = ProductSerializer
    purchase = PurchaseSerializer
    validators = [
        UniqueTogetherValidator(
            queryset=PurchaseLine.objects.all(),
            fields=["purchase", "product"],
            message="Ya tienes ese producto en tu carrito",
        )
    ]

    NOT_FOUND_EXCEPTION = exceptions.NotFound(
        {"purchase": "No pudimos encontrar tu carrito 🥺"}
    )

    class Meta:
        model = PurchaseLine
        fields = [
            "id",
            "purchase",
            "product",
        ]

    def validate(self, data):
        purchase = data.get("purchase", None)
        product = data.get("product", None)

        self.check_purchase(purchase)
        self.check_product(product)
        self.validate_number_of_lines(purchase)

        return data

    @staticmethod
    def validate_number_of_lines(purchase):
        if purchase.lines.count() >= 2:  # Todo Check this validation, is more complex
            raise exceptions.ValidationError(
                {
                    "purchase": "Ya tienes 2 productos en tu carrito, no puedes añadir más 🥺"
                }
            )

    def check_purchase(self, purchase):
        if not purchase:
            raise self.NOT_FOUND_EXCEPTION

        if purchase.state in [
            PurchaseWorkflow.Choices.CANCELED,
            PurchaseWorkflow.Choices.APPROVED,
        ]:
            raise self.NOT_FOUND_EXCEPTION

        if purchase.state == PurchaseWorkflow.Choices.CONFIRMED:
            raise exceptions.ValidationError(
                {"purchase": "Tienes una compra pendiente de aprobación"}
            )

    def check_product(self, product):
        if not product:
            raise self.NOT_FOUND_EXCEPTION

        if not product.can_be_sold:
            raise exceptions.ValidationError(
                {"product": f"El producto {product} no se puede vender 🥺"},
            )

        if product.available_stock < 0:
            raise exceptions.ValidationError(
                {"product": f"El producto {product} no tiene stock 🥺"}
            )
