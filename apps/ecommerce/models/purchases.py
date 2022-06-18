"""Models to purchases"""

from django.db import models

# Models
from django.db.models.signals import post_save, post_delete
from django_fsm import FSMIntegerField
from tracing.models import BaseModel

from apps.ecommerce.signals import reserve_stock, cancel_reserve_stock
from apps.ecommerce.transitions import PurchaseTransitions


class Purchase(BaseModel, PurchaseTransitions):
    workflow = PurchaseTransitions.workflow

    state = FSMIntegerField(
        choices=workflow.choices,
        default=workflow.CREATED,
        protected=True,
        verbose_name="estado",
    )

    user = models.ForeignKey(
        to="authentication.User",
        verbose_name="usuario",
        on_delete=models.PROTECT,
        null=False,
    )

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"


class PurchaseLine(BaseModel):
    product = models.ForeignKey(
        to="products.Product",
        verbose_name="Producto",
        on_delete=models.SET_NULL,
        null=True,
        related_name="purchase_lines",
    )
    purchase = models.ForeignKey(
        to="ecommerce.Purchase",
        verbose_name="Compra",
        on_delete=models.PROTECT,
        null=False,
        related_name="lines",
    )

    class Meta:
        verbose_name = "línea de compra"
        verbose_name_plural = "líneas de compra"


post_save.connect(reserve_stock, sender=PurchaseLine)
post_delete.connect(cancel_reserve_stock, sender=PurchaseLine)
