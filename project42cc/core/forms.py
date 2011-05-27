from django.forms import ModelForm

from core.models import Person
from core.widgets import CalendarWidget


class PersonForm(ModelForm):
    class Meta:
        model = Person
        widgets = {'birth_date':  CalendarWidget}

    class Media:
        js = (
            '/static/js/jquery-1.4.2.min.js',
            '/static/js/jquery.form.js',
            '/static/js/jquery.populate.js',
            '/static/js/custom.js',
        )
