from rest_framework import serializers

from .models import Product



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class FavoritesCreateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

    def validate(self, data):
        id_ = data.get("product_id")
        try:
            Product.objects.get(pk=id_)
        except Product.DoesNotExist:
            raise serializers.ValidationError({"error": "Product does not exist"})
        else:
            return data



        
