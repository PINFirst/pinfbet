from django.test import TestCase
from django.urls import reverse
from .models import User
from .models import Student


class TestUrlsMixing(TestCase):
    def setUp(self):
        self.name = 'elpepe'
        self.password = '7878'
        self.user = User.objects.get_or_create(username='testuser')[0]
        self.student = Student.objects.create(user=self.user)

    def protected_url(self, url, args=None):
        if not args:
            response = self.client.get(reverse(url))
            self.assertEqual(response.status_code, 302)
            self.client.force_login(user=self.user)
            response = self.client.get(reverse(url))
            self.assertEqual(response.status_code, 200)
        else:
            response = self.client.get(reverse(url, args=[args]))
            self.assertEqual(response.status_code, 302)
            self.client.force_login(user=self.user)
            response = self.client.get(reverse(url, args=[args]))
            self.assertEqual(response.status_code, 200)


class FeedViewTest(TestUrlsMixing):
    def test_feed_url(self):
        """
        Auth access to feed url view (logged and unlogged)
        """
        self.protected_url('feed')


class ProfileViewTest(TestUrlsMixing):
    def test_profile_url(self):
        """
        Auth access to profile url view (logged and unlogged)
        """
        self.protected_url('profile')


class BetsViewTest(TestUrlsMixing):
    def test_bet_url(self):
        """
        Auth access to bets url view (logged and unlogged)
        """
        self.protected_url('bets')


class FriendViewTest(TestUrlsMixing):
    def test_friend_url(self):
        """
        Auth access friend url view (logged and unlogged)
        """
        self.protected_url('view', self.user.id)
