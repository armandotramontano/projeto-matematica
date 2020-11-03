from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudante, User, Professor, Questao, Alternativa
from django.utils import timezone
from .forms import EstudanteForm


# Create your views here.

def home(request):
    estudantes = Estudante.objects.order_by('nome_completo')
    professores = Professor.objects.order_by('nome_completo')
    tabela = Estudante.objects.all()
    tabela2 = User.objects.all()
    return render(request, 'matematicaapp/home.html', {'estudantes': estudantes, 'tabela': tabela, 'tabela2': tabela2, 'professores': professores})
    
def atividadesgratis(request):
    questoes = Questao.objects.all()
    return render(request, 'matematicaapp/atividadesgratis.html', {'questoes': questoes})

def atividades5ano(request, pk, id_resposta):
    questao = get_object_or_404(Questao, pk=pk)
    alternativas = Alternativa.objects.filter(questao=pk)
    resposta = Alternativa.objects.filter(pk=id_resposta)
    return render(request, 'matematicaapp/atividades5ano.html', {'questao': questao, 'alternativas': alternativas, 'resposta':resposta})

def estudante_detail(request, pk):
    estudante = get_object_or_404(Estudante, pk=pk)
    return render(request, 'matematicaapp/estudante_detail.html', {'estudante': estudante})    

def estudante_novo(request):
    if request.method == "POST":
        form = EstudanteForm(request.POST)
        if form.is_valid():
            estudante = form.save(commit=False)
           # estudante.nome_completo = request.user
            estudante.created_date = timezone.now()
            estudante.save()
            return redirect('estudante_detail', pk=estudante.pk)
    else:
        form = EstudanteForm()
    return render(request, 'matematicaapp/estudante_edit.html', {'form': form})

def estudante_edit(request, pk):
    estudante = get_object_or_404(Estudante, pk=pk)
    if request.method == "POST":
        form = EstudanteForm(request.POST, instance=estudante)
        if form.is_valid():
            estudante = form.save(commit=False)
            # estudante.nome_completo = request.user
            estudante.updated_date = timezone.now()
            estudante.save()
            return redirect('estudante_detail', pk=estudante.pk)
    else:
        form = EstudanteForm(instance=estudante)
    return render(request, 'matematicaapp/estudante_edit.html', {'form': form})

    