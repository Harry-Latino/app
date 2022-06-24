"""Models to purchases"""
from django.core.exceptions import ValidationError
from django.db import models

# Models
from django.db.models.signals import post_save, post_delete
from django.utils.text import capfirst, get_text_list
from django_fsm import FSMIntegerField
from tracing.models import BaseModel

from apps.ecommerce.signals import reserve_stock, cancel_reserve_stock
from apps.ecommerce.transitions import PurchaseTransitions
from django.utils.translation import gettext_lazy as _


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

    def __str__(self):
        return f"{self.user.__str__()} - {self.get_created_date} ({self.get_state_display()})"

    @property
    def get_created_date(self):
        return self.created_date.strftime("%d/%m/%Y")

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
        unique_together = ["product", "purchase"]


post_save.connect(reserve_stock, sender=PurchaseLine)
post_delete.connect(cancel_reserve_stock, sender=PurchaseLine)
