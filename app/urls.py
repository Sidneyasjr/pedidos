from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pedido', views.create, name='order'),
    path('editar/<int:order_id>/', views.update, name='edit'),
]
