import io

import environ
import os
from pathlib import Path

import google.auth
from google.cloud import secretmanager

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DJANGO_SETTINGS_SECRET_NAME = 'django-settings'

env = environ.Env(
    DEBUG=(bool, False)
)
env_file = os.path.join(BASE_DIR, ".env")

_, os.environ["GOOGLE_CLOUD_PROJECT"] = google.auth.default()

if os.path.isfile(env_file):
    env.read_env(env_file)

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", None)

if not project_id:
    raise Exception("Project ID was not loaded correctly. Check service account credentials.")


# Get Django settings for a Cloud Run deployment
if os.environ.get("GCLOUD_DEPLOYMENT"):
    client = secretmanager.SecretManagerServiceClient()
    secret_name = f"projects/{project_id}/secrets/{DJANGO_SETTINGS_SECRET_NAME}/versions/latest"
    secret_data = client.access_secret_version(name=secret_name).payload.data.decode("UTF-8")

    # Save to env variables
    env.read_env(io.StringIO(secret_data))


DEBUG = os.getenv('DEBUG')

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "insecure_key")

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0", ".ew.r.appspot.com", ".a.run.app"]

# CSRF settings

CSRF_COOKIE_DOMAIN = 'https://*.a.run.app'

CSRF_TRUSTED_ORIGINS = ['https://*.a.run.app']

# Application definition

INSTALLED_APPS = [
    "products.apps.ProductsConfig",
    "django_extensions",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "trastero.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "trastero.wsgi.application"

DATABASES = {'default': env.db()}

if os.getenv("USE_CLOUD_SQL_AUTH_PROXY", None):
    DATABASES["default"]["HOST"] = "127.0.0.1"
    DATABASES["default"]["PORT"] = 5432


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
