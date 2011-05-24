from StringIO import StringIO
from django.core.management import call_command
from django.utils import unittest
from django.test.client import Client
from django.template import Template, Context, RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from core.models import Person, Log


class ViewsTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.user = User.objects.create_user('username',
            'user@mail.com', 'password')

    def tearDown(self):
        self.user.delete()

    def test_index(self):
        # Issue a GET request.
        url = reverse('core.views.index')
        response = self.client.get(url)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        url = reverse('django.contrib.auth.views.login')
        self.client.post(url, {
            'username': 'username',
            'password': 'password',
            })

        self.assertEqual(self.user.is_authenticated(), True)

    def test_edit_person(self):
        self.client.login(username='username', password='password')
        url = reverse('core.views.edit_person')
        response = self.client.post(url, {
            'name': 'AddName',
            'surname': 'AddSurname'
            })
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the Person is present in db
        try:
            person = Person.objects.get(name__exact='AddName',
                            surname__exact='AddSurname')
        except Person.DoesNotExist:
            person = None
        self.assertNotEqual(person, None)


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
        url = reverse('core.views.index')
        resp = client.get(url)
        debug_template = Template('{{settings.DEBUG}}')
        debug = debug_template.render(RequestContext(resp.request))
        self.assertNotEqual(len(debug), 0)


class ContextTest(unittest.TestCase):
    def test_context(self):
        person = Person.objects.create(name='ContextName',
                 surname='ContextSurname')
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
        next_count = len(Log.objects.all())
        self.assertNotEqual(next_count - prev_count, 0)
