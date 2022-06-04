"""Define mixins to list and edit profile"""

# Local
from django.shortcuts import redirect
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
        to_users_id = [profile.forum_user_id]
        moderator = self.request.user.forum_user_id
        if moderator and moderator != profile.forum_user_id:
            to_users_id.append(moderator)
        title = "Cuenta en el Magic Mall creada correctamente"
        body = "HTML generado"
        to_users_id_cleaned = ""

        for user_id in to_users_id:
            to_users_id_cleaned += f"&to[]={user_id}"

        APIService.download_user_data_and_update(profile)
        APIService.send_personal_message(to_users_id=to_users_id_cleaned, title=title, body=body)

        if profile.user:
            user = profile.user
        else:
            user = User.objects.create_user(username=profile.nick, password=str(self.object.token), profile=profile)
        self.object.user = user
        self.object.save()

        return redirect(site_url(self.object, "detail"))
