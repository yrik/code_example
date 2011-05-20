from django.shortcuts import render_to_response
from django.template import RequestContext

from core.models import Person


def index(request):
    persons = Person.objects.filter(pk=1)
    return render_to_response('index.html', {'persons': persons},
                                context_instance=RequestContext(request))
