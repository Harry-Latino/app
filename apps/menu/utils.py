"""Util to extract url from site"""

# Django
from django.urls import NoReverseMatch

# Third party integration
from superadmin import site
from superadmin.shortcuts import get_urls_of_site


def get_site_url(instance, action):
    model_site = site.get_modelsite(instance.__class__)
    urls = get_urls_of_site(model_site, instance)
    if action in urls:
        return urls[action]
    raise NoReverseMatch("The action '%s' doesn't exist in the model" % action)
