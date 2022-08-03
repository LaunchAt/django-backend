from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from project.db.actions import (
    delete_queryset,
    hard_delete_queryset,
    restore_queryset,
)
from project.db.utils import STATIC_URL

__all__ = [
    'DeletableMixin',
    'ForcedUndeletableMixin',
    'SoftDeletableMixin',
    'RestorableMixin',
    'ForcedUneditableMixin',
    'BaseModelAdmin',
]


yes_icon_image_html = mark_safe(
    f'<img src="{STATIC_URL}/project_db/img/icon-yes.svg" alt="True">'
)


no_icon_image_html = mark_safe(
    f'<img src="{STATIC_URL}/project_db/img/icon-no.svg" alt="False">'
)


class DeletableMixin(admin.ModelAdmin):
    def get_actions(self, request):
        self.admin_site.add_action(hard_delete_queryset)
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class ForcedUndeletableMixin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, *args, **kwargs):
        return False


class SoftDeletableMixin(admin.ModelAdmin):
    def get_actions(self, request):
        self.admin_site.add_action(delete_queryset)
        return super().get_actions(request)

    @admin.display(description=_('deleted'))
    def is_deleted(self, obj):
        return no_icon_image_html if obj.is_deleted else yes_icon_image_html


class RestorableMixin(admin.ModelAdmin):
    def get_actions(self, request):
        self.admin_site.add_action(restore_queryset)
        return super().get_actions(request)

    @admin.display(description=_('deleted'))
    def is_deleted(self, obj):
        return no_icon_image_html if obj.is_deleted else yes_icon_image_html


class ForcedUneditableMixin(admin.ModelAdmin):
    def has_change_permission(self, *args, **kwargs):
        return False


class ForcedUnaddableMixin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs):
        return False


class BaseModelAdmin(
    SoftDeletableMixin,
    RestorableMixin,
    DeletableMixin,
):
    pass
