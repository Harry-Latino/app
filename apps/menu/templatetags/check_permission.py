"""Sim templatetags"""
# Django
from django import template
from django.db.models import Sum
from django.urls import NoReverseMatch
from django.contrib.contenttypes.models import ContentType

# Third party integration
from superadmin import site
from superadmin.shortcuts import get_urls_of_site

# Local
from ..utils import get_site_url as get_url

register = template.Library()


@register.simple_tag
def check_permission(user, permission):
    if user.is_superuser:
        return True
    return user.has_perm(permission)


@register.simple_tag
def concat_all(*args):
    """concatenate all args"""
    return "".join(map(str, args))


@register.simple_tag
def sum_sales_products_queryset(queryset):
    aggregation = queryset.aggregate(Sum("product__points"))
    return aggregation.get("product__points__sum") or 0
