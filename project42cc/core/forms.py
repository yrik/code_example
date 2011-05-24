from django.forms import ModelForm

from core.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
