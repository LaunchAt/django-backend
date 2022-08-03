from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _('Admin Site')

admin.site.site_title = _('Admin Site')

admin.site.index_title = _('Dashboard')

admin.site.site_url = settings.SERVICE_CLIENT_URL

admin.site.enable_nav_sidebar = True

urlpatterns = []

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

urlpatterns.append(path('', admin.site.urls))
