from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DataViewSet, DeviceViewSet

router = DefaultRouter()
router.register('value', DataViewSet)
router.register('device', DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]