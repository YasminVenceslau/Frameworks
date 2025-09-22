# portifolio/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post

# Página inicial mostrando apenas posts publicados
def home(request):
    posts = Post.objects.filter(status='published').order_by('-criado_em')
    return render(request, 'index.html', {'posts': posts})

class PostDetails(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'         # campo do modelo usado para lookup
    slug_url_kwarg = 'slug'     # nome do parâmetro na URL