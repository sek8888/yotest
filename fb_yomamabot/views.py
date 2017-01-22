from django.views import generic
from django.http.response import HttpResponse
# Create your views here.

class YoMamaBotView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('qwer')
    def index(request):
    # return HttpResponse('Hello from Python!')
    return HttpResponse('qwer')
