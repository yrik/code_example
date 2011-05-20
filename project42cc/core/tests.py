from django.utils import unittest
from django.test.client import Client
from django.template import Template, RequestContext

from core.models import Person


class ViewsTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_index(self):
        # Issue a GET request.
        response = self.client.get('/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


class ModelsTest(unittest.TestCase):
    def test_person(self):
        person = Person(name='name', surname='sur', bio='bio')
        person.save()
        self.assertEqual(person.name, 'name')
        self.assertEqual(person.surname, 'sur')
        self.assertEqual(person.bio, 'bio')


class ContextTest(unittest.TestCase):
    def test_context(self):
        client = Client()
        resp = client.get('/')
        debug_template = Template('{{settings.DEBUG}}')
        debug = debug_template.render(RequestContext(resp.request))
        self.assertNotEqual(len(debug), 0)
