"""View to show update profile"""
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
from superadmin.views import DetailView
from .sites import UserProfileSite
from .models import User, AccessToken


class UserProfile(DetailView):
    site = UserProfileSite(User)


class LoginWithToken(DetailView):
    """Rewrite Detail View to Login with token"""

    model = AccessToken
    slug_field = "token"
    template_name = "base.html"

    def get(self, request, *args, **kwargs):
        """Validate user and login"""
        # self.object = AccessToken.objects.get(token=kwargs["uuid"])
        self.object = self.get_object()
        login(request, self.object.user)
        messages.success(request, "Te autenticaste correctamente")
        return redirect("/")
