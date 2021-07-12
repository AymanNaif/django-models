from django.test import TestCase

from django.urls import reverse
# Create your tests here.


class SnacksTest(TestCase):
    def test_snack_status_code(self):
        url = reverse('snack-list')
        actual = self.client.get(url).status_code
        expected = 200
        self.assertEqual(expected, actual)

    def test_snack_template(self):
        url = reverse('snack-list')
        response = self.client.get(url)
        actual = 'snack-list.html'
        self.assertTemplateUsed(response, actual)
