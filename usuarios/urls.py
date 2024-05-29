from  django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('gerenciar-conta/', views.gerenciar_conta, name='gerenciar_conta'),
    path('gerenciar-conta/criar-conta/', views.criar_conta, name='criar_conta'),
    path('gerenciar-conta/editar-dados/<int:id_usuario>', views.editar_dados, name='editar_dados'),
    path('gerenciar-conta/deletar-conta/<int:id_usuario>', views.deletar_conta, name='deletar_conta'),
    path('gerenciar-conta/deletar-conta/confirmar-exclusao-dados/<int:id_usuario>', views.confirmar_exclusao_dados, name='confirmar_exclusao_dados'),
    
]