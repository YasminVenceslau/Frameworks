# portifolio/factories.py
import factory
from portifolio.models import Post, UserProfile


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    titulo = factory.Faker("sentence", nb_words=4)
    conteudo = factory.Faker("paragraph")


class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile

    nome = factory.Faker("name")
    email = factory.Faker("email")
