from django.db import models

# Modelo de posts do portfólio
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

# Modelo de usuários do portfólio
class UserProfile(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
