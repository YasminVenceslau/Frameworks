import pytest
from blog.factories import PostFactory

# Cria uma fixture que gera um post já publicado
@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')

# Teste que usa banco de dados do Django
@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'

