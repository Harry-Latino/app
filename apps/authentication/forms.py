# Django
from django import forms

# Models
from apps.authentication.models import User, AccessToken
from apps.profiles.models import Profile

# Third party integration
from superadmin.forms import ModelForm
from django_select2 import forms as s2forms


class UserForm(ModelForm):
    class Meta:
        model = User
        fieldsets = (("first_name", "last_name"),)


class AccessTokenForm(ModelForm):
    wizard = forms.ModelChoiceField(
        queryset=Profile.objects.all(),
        widget=s2forms.ModelSelect2Widget(
            model=Profile,
            search_fields=[
                "nick__icontains",
                "forum_user_id__icontains",
            ],
            max_results=100,
            attrs={
                "data-minimum-input-length": 0,
                "data-app": "territorialization",
                "data-model": "province",
            },
        ),
        label="Mago",
    )

    class Meta:
        model = AccessToken
        fieldsets = ("wizard", "user")
        widgets = {"user": forms.HiddenInput()}
