from django.test import TestCase
from horoscope.views import zodiac_dict
from django.urls import reverse


# Create your tests here.

class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_signs(self):

        for key, value in zodiac_dict.items():
            redirect_url = reverse('horoscope-name', args=[key])
            response = self.client.get(redirect_url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(value, response.content.decode())

    def test_sign_redirect(self):
        for i, value in enumerate(zodiac_dict, start=1):
            redirect_url = reverse('horoscope-name', args=[i])
            redirect_url_value = reverse('horoscope-name', args=[value])
            response = self.client.get(redirect_url)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, redirect_url_value)


