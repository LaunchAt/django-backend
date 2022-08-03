from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _

from project.db.models import BaseModel
from project.user.manager import UserManager


class AbstractUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(
        _('username'),
        max_length=254,
        unique=True,
        help_text=_(
            'Required. 254 characters or fewer. '
            'Letters, digits and @/./+/-/_ only.'
        ),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
        blank=False,
        null=True,
        default=None,
    )
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    frozen_at = models.DateTimeField(
        _('frozen date-time'),
        blank=True,
        null=True,
        default=None,
        editable=False,
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS: list[str] = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
