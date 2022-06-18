"""Transitions for Sales"""
# Third party integration
from django_fsm import transition

# Local
from apps.ecommerce.workflows import PurchaseWorkflow


class PurchaseTransitions:
    workflow = PurchaseWorkflow()

    @transition(
        field="state",
        source=[
            workflow.CREATED,
        ],
        target=workflow.CONFIRMED,
        permission="purchases.add_purchase",
        custom=dict(verbose="Confirmar Compra"),
    )
    def confirm(self, **kwargs):
        pass
