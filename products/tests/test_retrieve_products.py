from unittest.mock import ANY

import pytest

from products.models import Product


@pytest.mark.django_db
class TestRetrieveProducts:
    def test_should_return_empty_list_when_no_products_exist(self, client):
        response = client.get("/api/products/")

        assert response.status_code == 200
        assert response.json() == []

    def test_should_return_products_list(self, client):
        Product.objects.create(
            name="Opel Corsa", description="Vendo opel corsa", price=5.00
        )

        response = client.get("/api/products/")

        assert response.status_code == 200
        assert response.json() == [
            {
                "id": ANY,
                "name": "Opel Corsa",
                "description": "Vendo opel corsa",
                "price": 5.00,
            }
        ]
