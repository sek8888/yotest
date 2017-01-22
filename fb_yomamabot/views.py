from django.views import generic
from django.http.response import HttpResponse
import time
# Create your views here.
class YoMamaBotView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(time.asctime())