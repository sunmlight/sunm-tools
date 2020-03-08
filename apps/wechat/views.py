import hashlib
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .we_msg import get_msg
import datetime
import time
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import xml.etree.ElementTree as ET
import time
import datetime
import cmn
import os


# Create your views here.
class Index(generic.View):
    def get(self, request):
        signature = request.GET.get("signature")
        timestamp = request.GET.get("timestamp")
        nonce = request.GET.get("nonce")
        echostr = request.GET.get("echostr")
        if signature and timestamp and nonce and echostr:
            token = settings.WECHATAPI["TOCKEN"]
            dlist = [token, timestamp, nonce]
            dlist.sort()
            hashstr = "".join([s for s in dlist])
            hashstr = hashlib.sha1(hashstr.encode()).hexdigest()
            if hashstr == signature:
                return HttpResponse(echostr)
        return HttpResponse("Error")

    # get msg from user
    def post(self, request):
        r = get_msg(request.body)
        return HttpResponse(r)

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(Index, self).dispatch(*args, **kwargs)
