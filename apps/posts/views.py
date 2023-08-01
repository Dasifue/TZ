from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from ..authe.models import User

from .serializers import (
    ProductSerializer,
    FavoritesCreateSerializer
)

class ProductsListApiView(ListAPIView):
    serializer_class = FavoritesCreateSerializer
    queryset = Product.objects.all()

    def get(self, request):
        serializer = ProductSerializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FavoritesCreateSerializer(data=request.data)
        user: User = request.user
        if user.is_authenticated:
            if serializer.is_valid():
                product = Product.objects.get(pk=serializer.validated_data["product_id"])
                if product not in user.favorites.all():
                    user.favorites.add(product)
                    return Response({"detail": "Success"}, status=status.HTTP_201_CREATED)
                return Response({"error": "Already in favorites"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "Login required"}, status=status.HTTP_401_UNAUTHORIZED)



class ProductsDetailsApiView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    
class FavoritesApiView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user: User = self.request.user
        return user.favorites.all()
    

class FavoritesDeleteApiView(RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user: User = self.request.user
        return user.favorites.all()
    
    def delete(self, request, pk):
        user: User = request.user
        product = Product.objects.get(pk=pk)
        user.favorites.remove(product)
        return Response({"detail": "Deleted"}, status=status.HTTP_200_OK)
        

