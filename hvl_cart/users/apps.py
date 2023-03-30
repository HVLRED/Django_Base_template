from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "hvl_cart.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import hvl_cart.users.signals  # noqa F401
        except ImportError:
            pass
