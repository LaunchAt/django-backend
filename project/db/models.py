import uuid

from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from project.db.query import BaseModelManager

__all__ = [
    'UUIDPrimaryKeyMixin',
    'TimeStampedMixin',
    'SoftDeletableMixin',
    'BaseModel',
]


class UUIDPrimaryKeyMixin(models.Model):
    """UUID Primary Key Model Mixin
    Set a UUID field as a primary key field to `id`.

    Fields:
        id (UUIDField): The UUID primary key.
    """

    id = models.UUIDField(
        _('id'),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    """Time Stamped Model Mixin
    Add the `created_at` and `updated_at` fields.

    Fields:
        created_at (DateTimeField): The date-time when created the instance.
        updted_at (DateTimeField): The date-time when updated the instance.
    """

    created_at = models.DateTimeField(
        _('created date-time'),
        auto_now_add=True,
        db_index=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        _('updated date-time'),
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True


class SoftDeletableMixin(models.Model):
    """Soft Deletable Model Mixin
    Add the `deleted_at` field for soft deletion.

    Fields:
        deleted_at (DateTimeField): The date-time when deleted the instance.
    Property:
        is_deleted (bool): Deleted flag.
    """

    deleted_at = models.DateTimeField(
        _('deleted date-time'),
        blank=True,
        null=True,
        db_index=True,
        default=None,
        editable=False,
    )

    class Meta:
        abstract = True

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    def delete(self):
        if self.deleted_at:
            return

        self.deleted_at = now()
        self.save(update_fields=['deleted_at'])

        for obj in self._meta.related_objects:
            if obj.on_delete == models.CASCADE:
                obj.related_model.objects.filter(
                    **{
                        obj.field.name: self,
                    }
                ).delete()


class BaseModel(UUIDPrimaryKeyMixin, TimeStampedMixin, SoftDeletableMixin):
    """Based Model"""

    objects = BaseModelManager()

    class Meta:
        abstract = True
