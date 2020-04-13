from django.test import TestCase, Client
from django.urls import reverse


class BaseViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    # TEST URLS
    def test_index_url_exists(self):
        response = self.client.get(reverse("base:index"))
        self.assertEqual(response.status_code, 200)

    def test_term_and_condition_url_exists(self):
        response = self.client.get(reverse("base:terms"))
        self.assertEqual(response.status_code, 200)

    def test_privacy_url_exists(self):
        response = self.client.get(reverse("base:privacy"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_url_redirects_when_not_logged_in(self):
        response = self.client.get(reverse("base:dashboard"))
        self.assertEqual(response.status_code, 302)
