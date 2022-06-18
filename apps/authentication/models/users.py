"""User model."""

# Django
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model."""

    created = models.DateTimeField(
        verbose_name="created at",
        auto_now_add=True,
        help_text="Datetime on which the user was created",
    )
    modified = models.DateTimeField(
        verbose_name="modified at",
        auto_now=True,
        help_text="Datetime on which the user was last modified",
    )
    old_number = models.IntegerField(verbose_name="ID anterior", null=True, blank=True)
    forum_user_id = models.IntegerField(
        verbose_name="ID del foro", null=True, blank=True
    )
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        """Return username."""
        return self.username

    class Meta(AbstractUser.Meta):
        """Class Meta."""

        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class AccessToken(models.Model):
    """Create a random token for login"""

    token = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="token")

    class Meta(AbstractUser.Meta):
        """Class Meta."""

        verbose_name = "Token de acceso"
        verbose_name_plural = "Tokens de acceso"

    def __str__(self):
        return f"Código de Acceso de {self.user.__str__()}"

    @property
    def profile(self):
        return self.user.profile

    @property
    def get_login_url(self):
        pass
