from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product


class RetrieveProductsView(APIView):
    def get(self, request):
        all_products = Product.objects.all()
        response_data = [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price} for product in all_products]
        return Response(status=HTTPStatus.OK, data=response_data)
