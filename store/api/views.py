from rest_framework.response import Response
from rest_framework.views import APIView

from store.api.serializers import ProductSerializer
from store.models import Product


class ProductList(APIView):

    def get_products(self):
        return Product.objects.all()

    def get(self, request):
        products = self.get_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
