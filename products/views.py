from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveProductsView(APIView):

    def get(self, request):
        return Response(status=HTTPStatus.OK, data=[{
            'id': 1,
            'name': 'Opel Corsa',
            'description': 'Vendo opel corsa',
            'price': 5.00
        }])
