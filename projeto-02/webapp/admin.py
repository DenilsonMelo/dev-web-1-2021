from django.contrib import admin
from .models import Aluno

# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'periodo_ingresso', 'nota', 'situacao')

admin.site.register(Aluno, AlunoAdmin)