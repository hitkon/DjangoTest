from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


class indexView(generic.TemplateView):
    template_name = "online_shop/index.html"


def index(request):
    return render(request, template_name='online_shop/index.html')
    #return HttpResponse("Shortcut for main page!")

