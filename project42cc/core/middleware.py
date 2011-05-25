from core.models import HTTP


class HTTPMiddleware(object):
    def process_request(self, request):
        HTTP.objects.create(value=repr(request))
        return None
