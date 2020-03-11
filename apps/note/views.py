from django.shortcuts import render

# Create your views here.
class Index(generic.View):
    def get(self, request):
        return HttpResponse('note')