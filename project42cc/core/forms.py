from django.forms import ModelForm

from core.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person

    class Media:
        js = (
            '/static/js/jquery-1.4.2.min.js',
            '/static/js/jquery.form.js',
            '/static/js/jquery.populate.js',
            '/static/js/custom.js',
        )
