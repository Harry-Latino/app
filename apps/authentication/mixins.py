"""Define mixins to list and edit profile"""

# Local
from django.shortcuts import redirect
from django.template.loader import render_to_string
from superadmin.templatetags.superadmin_utils import site_url

from apps.authentication.models.users import User
from apps.utils.services import APIService


class UserListMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(pk=self.request.user.pk)
        return queryset


class UserProfileMixin:
    def get_object(self, queryset=None):
        return self.request.user


class AccessTokenCreateMixin:
    def form_valid(self, form):
        profile = form.cleaned_data.get("wizard")
        self.object = form.save(commit=False)

        profile = APIService.download_user_data_and_update(profile)

        if profile.user:
            user = profile.user
        else:
            user = User.objects.create_user(
                username=profile.nick, password=str(self.object.token), profile=profile
            )

        self.object.user = user
        self.object.save()
        self.object.refresh_from_db()
        self.object.send_message()

        return redirect(site_url(self.object, "detail"))
