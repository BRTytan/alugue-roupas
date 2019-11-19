from django.shortcuts import render

# Create your views here.

def home(request):
    nome = 'Groger'
    idade = 17
    lista_roupas = [
        'boné da lacoste',
        'Boné Cyclone',
        'cinto do batman',
        'Toca da Medusa',
        'Oculos rift zika'
    ]

    context = {
        'roupas':lista_roupas,
        'nome':nome,
        'idade':idade
    }
    return render(request, 'home.html', context)