# Local
from apps.workflows import WorkflowChoices, Workflow


class PurchaseWorkflow(Workflow):
    class Choices(WorkflowChoices):
        CANCELED = 0, "Cancelado", dict(visible=False)
        CREATED = 1, "Creado"
        CONFIRMED = 2, "Confirmado"
        APPROVED = 3, "Aprobado"
