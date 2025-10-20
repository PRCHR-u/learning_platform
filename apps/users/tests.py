from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User


class UserAuthAPITests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'StrongPassword123',
            'password2': 'StrongPassword123'
        }

    def test_user_registration(self):
        """Ensure a new user can be registered."""
        response = self.client.post(
            self.register_url, self.user_data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'test@example.com')

    def test_user_login(self):
        """Ensure a registered user can log in and get a token."""
        # First, register the user
        self.client.post(self.register_url, self.user_data, format='json')

        # Then, attempt to log in
        login_data = {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)

    def test_password_mismatch(self):
        """Ensure registration fails if passwords do not match."""
        mismatched_data = self.user_data.copy()
        mismatched_data['password2'] = 'WrongPassword123'
        response = self.client.post(
            self.register_url, mismatched_data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('password' in response.data)

    def test_unauthenticated_user_view(self):
        """Ensure that unauthenticated users can't access the user view."""
        # Assuming you have a 'user-list' or 'user-detail' view
        # that requires authentication. If not, this test needs adjustment.
        # Let's test a protected view from the other app, e.g., course-list
        protected_url = reverse('course-list')
        response = self.client.get(protected_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
