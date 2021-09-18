# Third party integration
from superadmin.decorators import register

# Base
from config.base import BaseSite

# Forms
from .forms import WorkMonthForm
from .mixins import WorkListMixin

# Filtering
from config.mixins import GenericFiltering


@register("payments.Work")
class WorkSite(BaseSite):
    detail_fields = ("wizard", "work", "work_description")
    list_fields = ("wizard", "work")
    paginate_by = 30
    form_class = WorkMonthForm
    list_mixins = (WorkListMixin,)


@register("payments.MonthPayment")
class MonthPaymentSite(BaseSite):
    detail_fields = ("month",)
    detail_template_name = None


@register("payments.MonthPaymentLine")
class MonthPaymentLineSite(BaseSite):
    pass


@register("payments.Post")
class PostSite(BaseSite):
    detail_fields = ("month",)
    fields = ("month",)
    detail_template_name = None


@register("payments.PropertyPayment")
class PropertyPaymentSite(BaseSite):
    detail_fields = (("month", "payment_type"),)
    list_fields = ("month", "payment_type")

    detail_template_name = None
    list_template_name = None
    list_mixins = (GenericFiltering,)
