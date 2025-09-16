from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # rota para a página inicial
    path('<slug:slug>/', views.PostDetails.as_view(), name='post_detail')  # se usar DetailView
]
