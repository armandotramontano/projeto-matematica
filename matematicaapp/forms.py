from django import forms
from .models import Estudante
from .models import Questao
from .models import Alternativa

class EstudanteForm(forms.ModelForm):

    class Meta:
        model = Estudante
        fields = ('nome_completo', 'cpf_responsavel',)

class QuestaoNovaForm(forms.ModelForm):

    class Meta:
        model = Questao
        # fields = ('enunciado', 'resposta','fonte', 'dificuldade', 'area', 'anos_de_escolaridade', 'figura',)
        fields = ('enunciado', 'resposta', 'figura',)

class QuestaoNovaAlternativaForm(forms.ModelForm):

    class Meta:
        model = Alternativa
        fields = ('conteudo',)


class AlternativaForm(forms.ModelForm):

    class Meta:
        model = Alternativa
        fields = ('conteudo', 'questao',)