from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def test_main(self):
        client=Client()
        response = client.get(reverse('recipe:main'))
        self.assertTemplateUsed(response, 'main.html')

    def test_category_list(self):
        client = Client()
        response = client.get(reverse('recipe:category_list'))
        self.assertTemplateUsed(response, 'category_list.html')
