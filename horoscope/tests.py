from django.test import TestCase
from horoscope.views import zodiac_dict


# Create your tests here.

class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        sign_zodiac_list = list(zodiac_dict)
        for sign in sign_zodiac_list:
            response = self.client.get(f'/horoscope/{sign}/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(zodiac_dict.get(sign), response.content.decode())

    def test_libra_redirect(self):
        response = self.client.get('/horoscope/7/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/horoscope/libra/')
