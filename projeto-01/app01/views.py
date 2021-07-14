from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def w3c(request):
    return render(request, 'w3c.html')

def html(request):
    return render(request, 'html.html')

def css(request):
    return render(request, 'css.html')

def javascript(request):
    return render(request, 'javascript.html')

def backend(request):
    return render(request, 'backend.html')

def frontend(request):
    return render(request, 'frontend.html')

