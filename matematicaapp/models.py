from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# from django.conf import settings
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    PROFESSOR = 'P'
    ESTUDANTE = 'E'
    TIPO = (
        (PROFESSOR, 'Professor'),
        (ESTUDANTE, 'Estudante'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO, unique=True, default=ESTUDANTE,)
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['tipo'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email
    


class Estudante(models.Model):
    ANOS_DE_ESCOLARIDADE = (
        ('1', '1º ano do EF'),
        ('2', '2º ano do EF'),
        ('3', '3º ano do EF'),
        ('4', '4º ano do EF'),
        ('5', '5º ano do EF'),
        ('6', '6º ano do EF'),
        ('7', '7º ano do EF'),
        ('8', '8º ano do EF'),
        ('9', '9º ano do EF'),
        ('10', '1º ano do EM'),
        ('11', '2º ano do EM'),
        ('12', '3º ano do EM'),
    )
    nome_completo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    cpf_responsavel = models.CharField(max_length=14)
    data_de_nascimento = models.CharField(max_length=10)
    ano_de_escolaridade = models.CharField(max_length=20, choices=ANOS_DE_ESCOLARIDADE, default='1')
    instituicao = models.TextField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    foto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
  
    def create(self):
        self.created_date = timezone.now()
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_completo



class Professor(models.Model):
    FORMACAO = (
        ('1', 'Curso Normal'),
        ('2', 'Graduação em Matemática'),
        ('3', 'Graduação em Pedagogia'),
    )
    nome_completo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_de_nascimento = models.CharField(max_length=10)
    formacao = models.CharField(max_length=20, choices=FORMACAO, default='2')
    instituicao = models.TextField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    foto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
  
    def create(self):
        self.created_date = timezone.now()
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_completo



class Questao(models.Model):
    DIFICULDADE = (
        ('1', 'facil'),
        ('2', 'medio'),
        ('3', 'dificil'),
    )
    AREA = (
        ('1', 'artmetica'),
        ('2', 'geometria'),
        ('3', 'algebra'),
    )
    ANOS_DE_ESCOLARIDADE = (
        ('1', '1º ano do EF'),
        ('2', '2º ano do EF'),
        ('3', '3º ano do EF'),
        ('4', '4º ano do EF'),
        ('5', '5º ano do EF'),
        ('6', '6º ano do EF'),
        ('7', '7º ano do EF'),
        ('8', '8º ano do EF'),
        ('9', '9º ano do EF'),
        ('10', '1º ano do EM'),
        ('11', '2º ano do EM'),
        ('12', '3º ano do EM'),  
    )    
    dificuldade = models.CharField(max_length=20, choices=DIFICULDADE, default='3')
    area = models.CharField(max_length=20, choices=AREA, default='3')
    anos_de_escolaridade = models.CharField(max_length=20, choices=ANOS_DE_ESCOLARIDADE, default='12')
    fonte = models.TextField()
    enunciado = models.TextField(max_length=100000)
    figura = models.FileField(upload_to='static/assets/questoes5ano', blank=True)
    resposta = models.IntegerField(default='1')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)


class Alternativa(models.Model):
    conteudo = models.CharField(max_length=20000)
    questao = models.ForeignKey(
        Questao, on_delete=models.CASCADE)
  