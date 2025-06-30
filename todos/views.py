from rest_framework import viewsets, permissions, filters
# from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Todo
from .serializers import UserSerializer, UserLoginSerializer, TodoSerializer
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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        
        response_data = serializer.data
        response_data.update(tokens)
        return Response(response_data, status=status.HTTP_201_CREATED)
        
class UserLoginView(generics.GenericAPIView):
    serializer_class =  UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'title']
    ordering = ['id']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)