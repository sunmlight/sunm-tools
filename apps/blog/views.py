from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse

# Create your views here.
class Index(generic.View):
    def get(self, request):
        return render(request, "base.html")
