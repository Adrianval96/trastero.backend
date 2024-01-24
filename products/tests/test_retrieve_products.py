import pytest


@pytest.mark.django_db
class TestRetrieveProducts:

    def test_foo(self, client):

        assert client.get('/products/').status_code == 200
