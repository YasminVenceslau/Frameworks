import pytest

from portifolio.factories import PostFactoy

@pytest.mark.django_db
def test_exemplo_soma():
    assert 1 + 1 == 2

@pytest.fixture
def post_published():
    return PostFactoy(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'