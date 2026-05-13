from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):

    html_template = 'home.html'
    PageVisit.objects.create(path=request.path)
    queryset = PageVisit.objects.all().order_by('-timestamp')
    return render(request, html_template, {'page_title': 'Home', 'visits': queryset})