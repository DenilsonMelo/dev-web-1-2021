from django.shortcuts import render
from webapp.models import Aluno

# Create your views here.
def index(request):
    alunos = Aluno.objects.all()

    chaveAlunos = {
        'alunos': alunos
    }

    return render(request,'index.html', chaveAlunos)

def aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    context = {
        'aluno': aluno
    }

    return render(request, 'aluno.html', context)