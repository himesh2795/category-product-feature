import traceback

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from feature.serializers.CategorySerializer import CategoryModel, CategorySerializer, CategoryTreeSerializer


class CategoryView(APIView):
    def get_sub_categories(self, category):
        pass

    def post(self, request, *args, **kwargs):
        try:
            serializer = CategorySerializer(data=request.data)
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
                category = CategoryModel.objects.get(pk=pk)
                serializer = CategorySerializer(category)
            else:
                categories = CategoryModel.objects.all()
                serializer = CategoryTreeSerializer(categories, many=True)

            return Response(serializer.data)

        except Exception as e:
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
