from django import forms
from .models import Estudante
from .models import Questao
from .models import Alternativa

class EstudanteForm(forms.ModelForm):

    class Meta:
        model = Estudante
        fields = ('nome_completo', 'cpf_responsavel',)

class QuestaoForm(forms.ModelForm):

    class Meta:
        model = Questao
        fields = ('enunciado', 'resposta',)

class AlternativaForm(forms.ModelForm):

    class Meta:
        model = Alternativa
        fields = ('conteudo', 'questao',)