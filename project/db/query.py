from typing import Any

from django.db.models import CASCADE
from django.db.models.manager import BaseManager
from django.db.models.query import QuerySet
from django.utils.timezone import now

__all__ = [
    'SoftDeletableQuerySet',
    'SoftDeletableManager',
    'BaseModelQuerySet',
    'BaseModelManager',
]


class SoftDeletableQuerySet(QuerySet):
    def hard_delete(self):
        return super().delete()

    def delete(self):
        for obj in self.model._meta.related_objects:
            if obj.on_delete == CASCADE:
                obj.related_model.objects.filter(
                    **{
                        f'{obj.field.name}__in': self,
                    }
                ).delete()
        return super().update(deleted_at=now())

    def restore(self):
        return super().update(deleted_at=None)

    def alive(self):
        return self.filter(deleted_at__isnull=True)

    def deleted(self):
        return self.filter(deleted_at__isnull=False)


ManagerFromSoftDeletableQuerySet: Any = BaseManager.from_queryset(
    SoftDeletableQuerySet
)


class SoftDeletableManager(ManagerFromSoftDeletableQuerySet):
    pass


class BaseModelQuerySet(SoftDeletableQuerySet):
    pass


ManagerFromBaseModelQuerySet: Any = BaseManager.from_queryset(
    BaseModelQuerySet
)


class BaseModelManager(ManagerFromBaseModelQuerySet):
    pass
