from django.shortcuts import render, HttpResponse



# Create your views here.
def home_page_view(request):
    return HttpResponse("<h1>Hello world</h1>")