from django.db import models
from django.contrib.auth.models import User
class Chefe(models.Model):
    nome = models.CharField(max_length=24)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    
    def __str__(self):
        return self.nome

class Configuracoes(models.Model):
    entrada1 = models.TimeField()#Não pode ser Null pq é nescesario ter ao menos uma entrada e saida 
    saida1 = models.TimeField()

    entrada2 = models.TimeField(null=True, blank=True)
    saida2 = models.TimeField(null=True, blank=True)

    def __str__(self):
        if self.saida2 == None:
            return str(self.entrada1) +" às "+ str(self.saida1)#so por questão de stetica
        else:
            return str(self.entrada1) +" às "+ str(self.saida2)

class Funcionario(models.Model): #models.SET_NULL
    nome = models.CharField(max_length=124)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    chefe = models.ForeignKey(Chefe, on_delete=models.CASCADE)#So coloquei isso pra funcionar. Não esta completo!
    configuracao = models.ForeignKey(Configuracoes, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=64)
    def __str__(self):
        return self.nome+"-"+self.cargo

class Frequencia(models.Model):
    #falta ter um relacionamento com Funcionario 
    data = models.DateField(auto_now_add=True)#Adicionei para poder fazer uma verificação nas Views(Sucesso, FrequenciaViews) linha:12 e 21
    entrada1 = models.TimeField(null=True, blank=True)
    saida1 = models.TimeField(null=True, blank=True)

    entrada2 = models.TimeField(null=True, blank=True)
    saida2 = models.TimeField(null=True, blank=True)
    status = models.BooleanField()
    tipo = models.BooleanField()
    ip = models.CharField(max_length=15, null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.data) 