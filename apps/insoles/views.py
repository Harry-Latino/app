"""View to response rendered templates """

# Django
from django.views.generic import View
from django.template.loader import render_to_string
from django.http import HttpResponseForbidden, JsonResponse
from django.urls import reverse_lazy
from django.apps import apps
from django.forms import modelform_factory

# Superadmin
from superadmin import site


class RenderFormView(View):
    """View to get record filtering by date"""

    http_method_names = ["get", "post"]

    def get_form_class(self, **kwargs):
        app_name = kwargs.get("app")
        model_name = kwargs.get("model")
        app = apps.get_app_config(app_name)
        model = app.get_model(model_name)
        model_site = site._registry[model]

        if model_site.form_class:
            form_class = model_site.form_class
        else:
            form_class = modelform_factory(model, fields=model_site.fields)

        return form_class

    def get(self, request, *args, **kwargs):

        app_name = kwargs.get("app")
        model_name = kwargs.get("model")

        if not self.request.user.has_perm(
            f"{app_name.lower()}.add_{model_name.lower()}"
        ):
            return HttpResponseForbidden()
        form_class = self.get_form_class(**kwargs)
        context = {
            "form": form_class(),
        }
        create_url = reverse_lazy("insoles_form", args=[app_name, model_name])
        template = render_to_string("insoles/form.html", context=context)
        res = {"create_url": create_url, "template": template, "app": app_name}

        return JsonResponse(res, status=200)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class(**kwargs)
        form = form_class(self.request.POST, self.request.FILES)

        if form.is_valid():
            instance = form.save()

        res = {
            "id": instance.id,
            "text": str(instance),
        }

        return JsonResponse(res, status=200)


class RenderFieldView(RenderFormView):
    """View to get record filtering by date"""

    http_method_names = [
        "get",
    ]

    def get(self, request, *args, **kwargs):
        app_name = kwargs.get("app")
        model_name = kwargs.get("model")
        field_name = kwargs.get("field")

        if not self.request.user.has_perm(f"{app_name}.change_{model_name}"):
            return HttpResponseForbidden()

        form_class = self.get_form_class(**kwargs)
        form = form_class()
        context = {"field": form[field_name]}
        template = render_to_string("insoles/field.html", context=context)
        res = {"template": template}

        return JsonResponse(res, status=200)
