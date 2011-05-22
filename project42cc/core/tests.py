from StringIO import StringIO
from django.core.management import call_command
from django.utils import unittest
from django.test.client import Client
from django.template import Template, Context, RequestContext

from core.models import Person, Log


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


class TemplateTagTest(unittest.TestCase):
    def test_edit_tag(self):
        client = Client()
        resp = client.get('/')
        debug_template = Template('{{settings.DEBUG}}')
        debug = debug_template.render(RequestContext(resp.request))
        self.assertNotEqual(len(debug), 0)


class ContextTest(unittest.TestCase):
    def test_context(self):
        person = Person.objects.create(name='Name', surname='Surname')
        person = Person.objects.get(pk=1)
        template = Template('{% load customtags %}{% edit_link person %}')
        context = Context({'person': person})
        edit_link = template.render(context)
        self.assertNotEqual(len(edit_link), 0)


class CommandTest(unittest.TestCase):
    def test_min_row_count(self):
        content = StringIO()
        call_command('statistic', stdout=content)
        content.seek(0)
        num = len(content.readlines())
        self.failUnless(num, 5)


class SignalTest(unittest.TestCase):
    def test_log(self):
        prev_count = len(Log.objects.all())
        Person.objects.create(name='Name', surname='Surname')
        next_count = len(Log.bjects.all())
        self.assertNotEqual(next_count - prev_count, 0)
