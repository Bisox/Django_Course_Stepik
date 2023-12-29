from django.test import TestCase


class TestGeometry(TestCase):

    def test_rectangle(self):
        response = self.client.get('/calculate_geometry/rectangle/3/5')
        self.assertEqual(response.status_code, 200)

    def test_rectangle_redirect(self):
        response = self.client.get('/calculate_geometry/get_rectangle_area/10/5')
        self.assertEqual(response.status_code, 302)
