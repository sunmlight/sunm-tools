from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import datetime
import time
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


# Create your views here.
class Index(generic.View):
    def get(self, request):
        return HttpResponse('notice')