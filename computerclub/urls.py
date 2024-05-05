from django.urls import path, include
from rest_framework import routers
from .views import DirectorViewSet, AdministratorViewSet, UserViewSet, OrderViewSet, OrderList

router = routers.DefaultRouter()
router.register('directors', DirectorViewSet)
router.register('administrators', AdministratorViewSet)
router.register('users', UserViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', OrderList.as_view())
]
