from django.test import TestCase
from todos.serializers import TodoSerializer, UserSerializer, UserRegistrationSerializer, UserLoginSerializer
from todos.models import User, Todo


class TodoSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="user@example.com",
            password="testpass",
            username= "testuser"
        )
        
        self.todo_data = {
            "title": "Test Todo",
            "description": "This is a test todo item.",
            "user": self.user
        }
        
    def test_valid_todo_serializer(self):
        serializer = TodoSerializer(data=self.todo_data)
        self.assertTrue(serializer.is_valid())
        
    def test_invalid_todo_serializer(self):
        invalid_data = {"description": "Missing title"}
        serializer = TodoSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        

class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="user2@example.com",
            username="user2",
            password="testpass2")
        
    def test_user_serializer(self):
        serializer = UserSerializer(instance=self.user)
        data = serializer.data
        self.assertEqual(data['email'], self.user.email)
        self.assertEqual(data['username'], self.user.username)
        
class UserRegistrationSerializerTestCase(TestCase):
    def test_valid_user_registration(self):
        data = {
            "email": "new@example.com",
            "password": "newpass",
            "username": "newuser"
        }
        serializer = UserRegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        
    def test_invalid_user_registration(self):
        data = {
            "email": "invalid-email",
            "password": "pass"
        }
        serializer = UserRegistrationSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        
class UserLoginSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="login@example.com", password="loginpass", username="loginuser")
        
    def test_valid_login(self):
        data = {
            "email": "login@example.com",
            "password": "loginpass"
        }
        serializer = UserLoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        
    def test_invalid_login(self):
        data = {
            "email": "login@example.com",
            "password": "wrongpass"
        }
        serializer = UserLoginSerializer(data=data)
        self.assertFalse(serializer.is_valid())

        