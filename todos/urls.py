from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet, UserRegistrationView, UserLoginView

# Create a router and register our viewset with it.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
]
