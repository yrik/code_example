from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


from core.models import Person, HTTP
from core.forms import PersonForm


def index(request):
    persons = Person.objects.filter(pk=1)
    return render_to_response('index.html',
                {'persons': persons},
                context_instance=RequestContext(request))


def requests(request):
    requests = HTTP.objects.all()[:10]
    return render_to_response('requests.html',
                {'requests': requests},
                context_instance=RequestContext(request))


@login_required(login_url='/login/')
def edit_person(request):
    success = False
    person = Person.objects.get(pk=1)
    if request.method == 'POST':  # If the form has been submitted...
        # A  form bound to the POST data
        form = PersonForm(request.POST,  instance=person)
        if form.is_valid():  # All validation rules pass
            form.save()
            success = True
    else:
        form = PersonForm(instance=person)  # An unbound form

    return render_to_response('edit_person.html',
        {'form': form, 'success': success},
        context_instance=RequestContext(request))
