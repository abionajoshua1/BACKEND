from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet, UserRegistrationView, UserLoginView, TodoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a router and register our viewset with it.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todos', TodoViewSet)

# The API URLs are now determined automatically by the router.


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
