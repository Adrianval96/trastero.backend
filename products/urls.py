from django.urls import path

from products.views import RetrieveProductsView

urlpatterns = [
    path('', RetrieveProductsView.as_view()),
]
