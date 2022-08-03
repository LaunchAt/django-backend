from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

# router.register('prefix', ModelViewSet)

urlpatterns = [path('', include(router.urls))]
