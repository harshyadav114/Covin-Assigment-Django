from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase

User = get_user_model()
client = APIClient()


class CreateExpenseTestCases(APITestCase):
    """
    Create Expense tests
    """
    
    def setUp(self):
        self.user1 = User.objects.create()
        