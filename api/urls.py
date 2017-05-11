from django.conf.urls import url, include
from rest_framework import routers

from .views import EmployerViewSet, EmployeeViewSet

# register our v1 api URL pattern
v1_router = routers.DefaultRouter()
v1_router.register(r'employers', EmployerViewSet, base_name='employer')
v1_router.register(r'employees', EmployeeViewSet, base_name='employee')

urlpatterns = [
    url(r'^v1/', include(v1_router.urls)),
]
