from django.test import TestCase
from todos.models import Todo, User

class TodoModelTest(TestCase):
    def test_create_todo(self):
        user = User.objects.create_user(
            email="test@gmail.com",
            password="testpassword",
        )
        
        todo = Todo.objects.create(
            user=user,
            title="Test Todo",
            description="This is a test todo item."
        )
        
        self.assertEqual(str(todo.title), "Test Todo")