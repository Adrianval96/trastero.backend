import pytest
from django.conf import settings


@pytest.fixture
def django_db_setup():
    settings.DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "test",
        }
    }
