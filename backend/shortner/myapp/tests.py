
from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from rest_framework.test import APIClient

from .models import ShortURL


class ShortURLTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    # Test 1: Create Short URL
    def test_create_short_url(self):

        response = self.client.post(
            '/api/shorten/',
            {
                'original_url': 'https://www.google.com'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            201
        )

        self.assertTrue(
            ShortURL.objects.filter(
                original_url='https://www.google.com'
            ).exists()
        )

    # Test 2: Redirect Short URL
    def test_redirect_short_url(self):

        response = self.client.post(
            '/api/shorten/',
            {
                'original_url': 'https://www.google.com'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            201
        )

        short_code = response.data['short_code']

        redirect_response = self.client.get(
            f'/{short_code}/'
        )

        self.assertEqual(
            redirect_response.status_code,
            302
        )

        self.assertEqual(
            redirect_response.url,
            'https://www.google.com'
        )

    # Test 3: Click Count
    def test_click_count(self):

        response = self.client.post(
            '/api/shorten/',
            {
                'original_url': 'https://www.google.com'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            201
        )

        short_code = response.data['short_code']

        url = ShortURL.objects.get(
            short_code=short_code
        )

        self.assertEqual(
            url.click_count,
            0
        )

        self.client.get(
            f'/{short_code}/'
        )

        url.refresh_from_db()

        self.assertEqual(
            url.click_count,
            1
        )

    # Test 4: Expired URL
    def test_expired_url(self):

        ShortURL.objects.create(
            original_url='https://www.google.com',
            short_code='TEST123',
            expires_at=timezone.now() - timedelta(hours=1)
        )

        response = self.client.get(
            '/TEST123/'
        )

        self.assertEqual(
            response.status_code,
            410
        )

    # Test 5: Invalid URL
    def test_invalid_urls(self):

        response = self.client.post(
            '/api/shorten/',
            {
                'original_url': 'hello'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            400
        )

        self.assertIn(
            'original_url',
            response.data
        )

