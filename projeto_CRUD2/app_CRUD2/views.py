from django.shortcuts import render

from .models import BancoDeDados


def home(request):
    
    bancoDeDados_variavel = BancoDeDados.objects.all()
    return render(request, "paginas/home.html", {"bancoDeDados_obj": bancoDeDados_variavel})
