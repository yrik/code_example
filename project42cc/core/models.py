from django.db import models


class Person(models.Model):
    """
    Person with properties
    """
    name = models.CharField(null=True, max_length=250)
    surname = models.CharField(null=True, max_length=250)
    bio = models.TextField(null=True, blank=True, max_length=250)
    other_contacts = models.TextField(null=True, blank=True, max_length=250)
    birth_date = models.DateField(null=True, blank=True)

    email = models.EmailField(null=True, blank=True, max_length=250)
    jabber = models.TextField(null=True, blank=True, max_length=250)
    skype = models.TextField(null=True, blank=True, max_length=250)

    def get_fields(self):
        return [(field.name, field.value_to_string(self))\
        for field in self._meta.fields]

    def __unicode__(self):
        return self.name + ' ' + self.surname

