import unittest
from django.test import Client, TestCase


class TestSearchPage(TestCase):

    def test_search_page_status_code(self):
        resp = self.client.get('/search')
        self.assertEqual(resp.status_code, 200)

    def test_search_page_with_query_returns_objects(self):
        import ipdb; ipdb.set_trace()
        resp = self.client.get('/search?query=cheese')
        self.assertEqual(resp.status_code, 200)
