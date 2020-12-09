from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudante, User, Professor, Questao, Alternativa
from django.utils import timezone
from .forms import EstudanteForm
from .forms import QuestaoNovaForm
from .forms import AlternativaForm
from .forms import QuestaoNovaAlternativaForm


# Create your views here.
def home(request):
    estudantes = Estudante.objects.order_by('nome_completo')
    professores = Professor.objects.order_by('nome_completo')
    tabela = Estudante.objects.all()
    tabela2 = User.objects.all()
    return render(request, 'matematicaapp/home.html', {'estudantes': estudantes, 'tabela': tabela, 'tabela2': tabela2, 'professores': professores})
    
    
def atividadesgratis(request):
    series = { "quinto": {"label": "Matemática - 5º ano", "image": "5ano.jpg"}, "sexto": {"label": "Matemática - 6º ano", "image": "6ano.jpg"}, "setimo": {"label": "Matemática - 7º ano", "image": "7ano.png"}, "oitavo": {"label": "Matemática - 8º ano", "image": "8ano.jpg"}, "nono": {"label": "Matemática - 9º ano", "image": "9ano.jpg"}, "concurso": {"label": "Matemática - Concurso Fundamental", "image": "concursofundamental.jpg"}, "primeiro": {"label": "Matemática - 1º ano EM", "image": "1ano.png"}, "segundo": {"label": "Matemática - 2º ano EM", "image": "2ano.jpg"}, "terceiro": {"label": "Matemática - 3º ano EM", "image": "3ano.jpg"}}
    questoes = Questao.objects.all()
    return render(request, 'matematicaapp/atividadesgratis.html', {'questoes': questoes, 'series': series})

def atividades5ano(request, pk, id_resposta):
    questao = get_object_or_404(Questao, pk=pk)
    proximo_pk = pk+1
    anterior_pk = pk-1
    alternativas = Alternativa.objects.filter(questao=pk)
    resposta = Alternativa.objects.filter(pk=id_resposta)
    return render(request, 'matematicaapp/atividades5ano.html', {'questao': questao, 'alternativas': alternativas, 'resposta':resposta, 'proximo_pk':proximo_pk, 'anterior_pk': anterior_pk})
    

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


def questao_nova(request):
    if request.is_ajax():
        print(request.POST)
        request_data = request.POST
        return HttpResponse("OK")
    if request.method == "POST":
        aform = QuestaoNovaForm(request.POST)
        bform = QuestaoNovaAlternativaForm(request.POST)
        if aform.is_valid() and bform.is_valid():
            questao = aform.save(commit=False)
            alternativas = bform.save(commit=False)
            questao.save()
            alternativas.save()
    else:
        aform = QuestaoNovaForm()
        bform = QuestaoNovaAlternativaForm(request.POST)
    return render(request, 'matematicaapp/questao_nova.html', {'aform': aform, 'bform': bform })

