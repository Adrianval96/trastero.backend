import pytest


@pytest.mark.django_db
class TestRetrieveProducts:

    def test_foo(self, client):

        response = client.get('/api/products/')

        assert response.status_code == 200
        assert response.json() == [
            {
                'id': 1,
                'name': 'Opel Corsa',
                'description': 'Vendo opel corsa',
                'price': 5.00
            }
        ]
