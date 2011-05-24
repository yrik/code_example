from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from core.models import Person
from core.forms import PersonForm


def index(request):
    persons = Person.objects.filter(pk=1)
    return render_to_response('index.html',
                {'persons': persons},
                context_instance=RequestContext(request))


@login_required(login_url='/login/')
def add_person(request):
    success = False
    if request.method == 'POST':  # If the form has been submitted...
        form = PersonForm(request.POST)  # A  form bound to the POST data
        if form.is_valid():  # All validation rules pass
            form.save()
            success = True
    else:
        form = PersonForm()  # An unbound form

    return render_to_response('add_person.html',
        {'form': form, 'success': success},
        context_instance=RequestContext(request))
