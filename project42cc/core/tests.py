import os
from StringIO import StringIO
from django.core.management import call_command
from django.utils import unittest
from django.test.client import Client
from django.template import Template, Context, RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings

from windmill.authoring import djangotest

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


class TemplateTagTest(unittest.TestCase):
    def test_edit_tag(self):
        client = Client()
        resp = client.get('/')
        debug_template = Template('{{settings.DEBUG}}')
        debug = debug_template.render(RequestContext(resp.request))
        self.assertNotEqual(len(debug), 0)


class ContextTest(unittest.TestCase):
    def test_context(self):
        person = Person(name='Name', surname='Surname')
        person.save()
        person = Person.objects.get(pk=1)
        template = Template('{% load customtags %}{% edit_link person %}')
        context = Context({'person': person})
        edit_link = template.render(context)
        self.assertNotEqual(len(edit_link), 0)


wmtests = settings.WINDMILL_TESTS

for name in os.listdir(wmtests):
    if name.startswith("test") and name.endswith(".py"):
        testname = name[:-3]

        class WindmillTest(djangotest.WindmillDjangoUnitTest):
            test_dir = os.path.join(wmtests, name)
            browser = "firefox"
        WindmillTest.__name__ = testname
        globals()[testname] = WindmillTest
        del WindmillTest
