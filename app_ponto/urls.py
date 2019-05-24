from django.urls import path
from .views import do_login , do_logout, Frequencia_View, erro, Sucesso, homePage

urlpatterns = [
    path('ponto', Frequencia_View, name='ponto'),
    path('', homePage.as_view(), name='home'),
    path('sucesso',Sucesso, name='sucesso'),
    path('login',do_login, name='login'),
    path('logout',do_logout, name='logout'),
    path('erro', erro, name='erro'),

]