from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudante
from django.utils import timezone
from .forms import EstudanteForm


# Create your views here.


def home(request):
    estudantes = Estudante.objects.order_by('nome_completo')
    return render(request, 'matematicaapp/home.html', {'estudantes': estudantes})

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