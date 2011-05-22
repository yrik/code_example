from django.db.models.signals import post_save, post_delete
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


class Log(models.Model):
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __unicode__(self):
        return '%s at %s' % (self.content, self.date)


def delete_callback(sender, instance, signal, *args, **kwargs):
    l = Log(content="object '%s' is deleted" % instance)
    l.save()

def save_callback(sender, instance, signal, *args, **kwargs):
    if sender != Log:
        if kwargs.get('created', True):
            l = Log(content="object '%s' is created" % instance)
        else:
            l = Log(content="object '%s' is edited" % instance)
        l.save()

post_save.connect(save_callback)
post_delete.connect(delete_callback)
