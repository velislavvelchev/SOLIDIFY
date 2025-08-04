from django.test import TestCase
from django.db import IntegrityError
from SOLIDIFY.accounts.models import AppUser


class AppUserModelTests(TestCase):

    def test_create_user_successfully(self):
        user = AppUser.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='strongpass123'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('strongpass123'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertIsInstance(user, AppUser)

    def test_create_superuser_successfully(self):
        admin = AppUser.objects.create_superuser(
            email='admin@example.com',
            username='adminuser',
            password='adminpass'
        )
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_duplicate_email_fails(self):
        AppUser.objects.create_user(
            email='duplicate@example.com',
            username='user1',
            password='testpass'
        )
        with self.assertRaises(IntegrityError):
            AppUser.objects.create_user(
                email='duplicate@example.com',
                username='user2',
                password='testpass'
            )

    def test_duplicate_username_fails(self):
        AppUser.objects.create_user(
            email='unique1@example.com',
            username='duplicateuser',
            password='testpass'
        )
        with self.assertRaises(IntegrityError):
            AppUser.objects.create_user(
                email='unique2@example.com',
                username='duplicateuser',
                password='testpass'
            )

    def test_string_representation_returns_email(self):
        user = AppUser.objects.create_user(
            email='str@example.com',
            username='struser',
            password='pass'
        )
        self.assertEqual(str(user), 'str@example.com')