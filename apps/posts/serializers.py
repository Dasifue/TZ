from rest_framework import serializers

from .models import Product

# Сериализаторы используются для преобразования python объектов в JSON формат и наоборот
# Прописал всего 2 сериализатора: 1 - для работы со всеми продуктами, 2 - для добавления продукта в фавориты 

class ProductSerializer(serializers.ModelSerializer):

    """
    Сериализатор выводит все поля продукта в формате JSON
    """

    class Meta:
        model = Product
        fields = "__all__"


class FavoritesCreateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

    """
    Сериализатор принимает в себя ID продукта, проверяет даные на валидность
    """


    def validate(self, data): #Метод validate вызывается самостоятельно в методе is_valid
        id_ = data.get("product_id") #Определяем отправленный пользователем id продукта
        try: #Проверям: существует ли продукт с введённым id
            Product.objects.get(pk=id_)
        except Product.DoesNotExist: #Если такого продукта не существует, то выводим ошибку
            raise serializers.ValidationError({"error": "Product does not exist"})
        else: #Иначе пропускаем данные
            return data



        
