from django.test import TestCase
from horoscope.views import zodiac_dict
from django.urls import reverse


# Create your tests here.

class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_signs(self):
        sign_zodiac_list = list(zodiac_dict)
        for sign in sign_zodiac_list:
            redirect_url = reverse('horoscope-name', args=[sign])
            response = self.client.get(redirect_url)
            self.assertEqual(response.status_code, 200)
            self.assertIn(zodiac_dict.get(sign), response.content.decode())

    def test_sign_redirect(self):
        for i in range(1, len(zodiac_dict)+1):
            response = self.client.get(f'/horoscope/{i}/')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{list(zodiac_dict)[i-1]}/')
