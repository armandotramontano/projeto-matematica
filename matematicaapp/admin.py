from django.contrib import admin
from .models import Estudante, User, Professor, Questao, Alternativa

# Register your models here.
admin.site.register(Estudante)
admin.site.register(User)
admin.site.register(Professor)
admin.site.register(Questao)
admin.site.register(Alternativa)