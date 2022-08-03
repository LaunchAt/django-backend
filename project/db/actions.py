from django.utils.translation import gettext_lazy as _

__all__ = [
    'hard_delete_queryset',
    'delete_queryset',
    'restore_queryset',
]


def hard_delete_queryset(modeladmin, request, queryset):
    return queryset.hard_delete()


setattr(hard_delete_queryset, 'allowed_permissions', ('delete',))
setattr(hard_delete_queryset, 'short_description', _('hard delete'))


def delete_queryset(modeladmin, request, queryset):
    return queryset.delete()


setattr(delete_queryset, 'allowed_permissions', ('delete',))
setattr(delete_queryset, 'short_description', _('soft delete'))


def restore_queryset(modeladmin, request, queryset):
    return queryset.restore()


setattr(restore_queryset, 'allowed_permissions', ('delete',))
setattr(restore_queryset, 'short_description', _('restore'))
