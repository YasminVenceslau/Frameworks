# portifolio/views.py

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post  # Certifique-se de que o modelo Post existe

# Função para a página inicial
def home(request):
    posts = Post.objects.all().order_by('-criado_em')  # pega todos os posts mais recentes primeiro
    return render(request, 'index.html', {'posts': posts})

# Classe para visualizar detalhes de um post
# Só habilite se você tiver o modelo Post e um template post_detail.html
class PostDetails(DetailView):
    model = Post  # modelo que será exibido
    template_name = 'post_detail.html'  # template que será usado
