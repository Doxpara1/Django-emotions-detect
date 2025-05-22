from django.urls import path,include
from .views import UserViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewset, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]