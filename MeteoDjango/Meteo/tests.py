

# Create your tests here.


from django.test import TestCase
from .models import CodeInse, Message

class CodeInse(TestCase):
    def test_model_creation(self):
        obj = CodeInse.objects.create(field1='test', field2=123)
        self.assertEqual(obj.field1, 'test')
        self.assertEqual(obj.field2, 123)

class Message(TestCase):
    def test_model_creation(self):
        obj = Message.objects.create(field1='test', field2=123)
        self.assertEqual(obj.field1, 'test')
        self.assertEqual(obj.field2, 123)
