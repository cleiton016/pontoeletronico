from django.contrib import admin
from .models import Chefe, Funcionario, Frequencia, Configuracoes
# Register your models here.
@admin.register(Chefe, Funcionario, Frequencia, Configuracoes)
class Pont(admin.ModelAdmin):
    pass