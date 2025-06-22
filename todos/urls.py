from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet

# Create a router and register our viewset with it.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.

urlpatterns = router.urls


