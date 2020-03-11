from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import datetime
import time
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from . import helper


# Create your views here.
class Index(generic.View):
    def get(self, request):
        return HttpResponse('warframe')


class GetKey(generic.View):
    def get(self, request):
        r = helper.get_wf_key()
        return HttpResponse('test') 