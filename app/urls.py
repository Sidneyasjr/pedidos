from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pedido', views.create, name='order'),
    path('editar/<int:id>/', views.update, name='edit'),
    path('deletar/<int:id>/', views.delete, name='delete'),
]
