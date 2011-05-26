from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.http import HttpResponse


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

        if request.is_ajax():
            result = {'success': success}
            data = form.data
            result.update({'data': data})
            if not success:
                d = {}
                for e in form.errors.iteritems():
                    d.update({e[0]: unicode(e[1])})
                result.update({'errors': d})

            json = simplejson.dumps(result, ensure_ascii=False)
            return HttpResponse(json, mimetype='application/javascript')

    else:
        form = PersonForm(instance=person)  # An unbound form

    return render_to_response('edit_person.html',
        {'form': form, 'success': success},
        context_instance=RequestContext(request))
