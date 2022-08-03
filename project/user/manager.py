from django.contrib.auth.models import UserManager as BaseUserManager

from project.db.query import BaseModelManager


class UserManager(BaseModelManager, BaseUserManager):
    pass
