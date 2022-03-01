import traceback

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from feature.serializers.ProductSerializer import ProductModel, ProductSerializer, ProductRetrieveSerializer


class ProductView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, *args, **kwargs):
        try:
            if pk:
                product = ProductModel.objects.get(pk=pk)
                serializer = ProductRetrieveSerializer(product)
            else:
                products = ProductModel.objects.all()
                serializer = ProductRetrieveSerializer(products, many=True)

            return Response(serializer.data)

        except Exception as e:
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        try:
            product = ProductModel.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            product = ProductModel.objects.get(pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
