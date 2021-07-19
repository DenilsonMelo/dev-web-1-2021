from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm

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

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

