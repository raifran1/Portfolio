from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'curriculo/index.html', {})

def page_secondary(request):
    return render(request, 'curriculo/teste.html', {})