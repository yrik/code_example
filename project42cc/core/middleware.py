from core.models import HTTP


class HTTPMiddleware(object):
    def process_request(self, request):
        HTTP.objects.create(value=obj_to_dict(request))
        return None


def obj_to_dict(obj):
    result = dict((key, repr(value)) for key, value in obj.__dict__.iteritems()
    if not callable(value) and not key.startswith('__'))
    return result
