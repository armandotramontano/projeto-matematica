from django.db import models
# from django.conf import settings
# Create your models here.


class Estudante(models.Model):
#    ANOS_DE_ESCOLARIDADE = (
#        (1, '1º ano do EF'),
#        (2, '2º ano do EF'),
#        (3, '3º ano do EF'),
#        (4, '4º ano do EF'),
#        (5, '5º ano do EF'),
#        (6, '6º ano do EF'),
#        (7, '7º ano do EF'),
#        (8, '8º ano do EF'),
#        (9, '9º ano do EF'),
#        (10, '1º ano do EM'),
#        (11, '2º ano do EM'),
#        (12, '3º ano do EM'),
#    )
    nome_completo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    cpf_responsavel = models.CharField(max_length=14)
    data_de_nascimento = models.CharField(max_length=10)
#    ano_de_escolaridade = models.CharField(max_length=2, choices=ANOS_DE_ESCOLARIDADE, default=1)
    instituicao = models.TextField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    foto = models.TextField()