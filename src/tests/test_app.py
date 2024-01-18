import pytest

from app import create_app


class TestApp:
    @pytest.fixture
    def mocked_app(self):
        app = create_app(
            {
                "TESTING": True,
            }
        )

        return app

    def test_hello_world(self, mocked_client):
        response = mocked_client.get("/")

        assert response.status_code == 200
        assert b"<p>Hello, World!</p>" in response.data
