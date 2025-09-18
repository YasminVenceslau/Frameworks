import pytest

@pytest.mark.django_db
def test_exemplo_soma():
    assert 1 + 1 == 2