from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime

# Create your views here.
def home(request):
    return HttpResponse ("olá,Django")

def home_view(request):
    """
    Renderiza a página inicial com um template HTML, passando a data e hora atuais como contexto.
    """
    context = {
        'data_e_hora': datetime.now() # Variável Python que será acessível no template HTML
    }
    return render(request, 'meuprimeiro_html.html', context) # Renderiza o template especificado

def login(reugest):
    nome = 'Giovanny'
    if nome == 'Guilherme':
        resposta ='Acesso liberado'
    else:
        resposta ='Acesso negado'    
    return HttpResponse(resposta)
