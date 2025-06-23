from rest_framework import viewsets
# from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserLoginView(generics.GenericAPIView):
    serializer_class =  UserLoginSerializer

    def post(self, reqquest):
        serializer = self.get_serializer(data=reqquest.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    