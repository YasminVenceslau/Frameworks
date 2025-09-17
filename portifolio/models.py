from django.db import models

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Rascunho'),
        ('published', 'Publicado'),
    )

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.titulo

