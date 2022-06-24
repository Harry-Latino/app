# Local
from apps.workflows import WorkflowChoices, Workflow


class UserTokenWorkflow(Workflow):
    class Choices(WorkflowChoices):
        CANCELED = 0, "Cancelado", dict(visible=False)
        SEND = 1, "Enviado"
