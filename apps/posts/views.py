from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Импортируем модели нашего проекта
from .models import Product
from ..authe.models import User


# Импортируем сериализаторы
from .serializers import (
    ProductSerializer,
    FavoritesCreateSerializer
)


# View выводит список всех продуктов и создаёт фавориты
class ProductsListApiView(ListAPIView):
    serializer_class = FavoritesCreateSerializer
    queryset = Product.objects.all()

    def get(self, request): #Переобрелелил метод для вывода всех постов используя сериализатор ProductSerializer
        serializer = ProductSerializer(instance=self.get_queryset(), many=True) #instance - Python объект, который должен быть преобразован в JSON, many=True, так как queryset возвращает множесвто объектов
        return Response(serializer.data, status=status.HTTP_200_OK) #Возвращаем ответ в виде JSON данных + добавляем статус запроса

    def post(self, request): #Создал метод для создания фаворитов авторизованного пользователя
        serializer = FavoritesCreateSerializer(data=request.data) #В сериализатор передаём JSON данные
        user: User = request.user #Определяем текущего пользователя
        if user.is_authenticated: #Проверяем: авторизован ли пользователь?
            if serializer.is_valid(): #Проверяем данные на валидность: в данном случае работает метод validate
                product = Product.objects.get(pk=serializer.validated_data["product_id"]) #Определяем продукт
                if product not in user.favorites.all(): # Проверяем: не находится ли продукв в фаворитах
                    user.favorites.add(product) # Добавляем пост в рекомендации

                    #Сообщаем пользователю о успешном запросе
                    return Response({"detail": "Success"}, status=status.HTTP_201_CREATED)
                
                #Если продукт находистя в фаворитах, то мы об этом сообщаем пользователю
                return Response({"error": "Already in favorites"}, status=status.HTTP_400_BAD_REQUEST)
            
            #Если не нашёлся продукт с введённым id, то выводится ошибка и статус 404
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
        #Если пользователь не авторизован, то выводится ошибка и статус 401
        return Response({"error": "Login required"}, status=status.HTTP_401_UNAUTHORIZED)
"""
Можно было не переопределять метод get, но для красоты на странице решил переопределить и его
"""


class ProductsDetailsApiView(RetrieveAPIView):
    """
    View для детальной страницы продукта
    метод get уже реализован в классе RetrieaveAPIView
    работает через передачу pk продукта в url
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    
class FavoritesApiView(ListAPIView):
    """
    View для вывода списка фаворитов аудентифицированного пользователя
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated] #Ограничение метода на работу только с авторизованными пользователями

    def get_queryset(self): #Метод определяет queryset запрос для набора выводимых данных. 
        user: User = self.request.user #Определяем авторизованного пользователя
        return user.favorites.all() #Создаём queryset запрос, выводящий все фавориты пользователя
    

class FavoritesDeleteApiView(RetrieveDestroyAPIView):
    """
    View для удаления продукта из фаворитов

    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated] #Пользователь должен быть авторизован

    def get_queryset(self):
        """
        View будет работать только с действительными фаворитами пользователя
        """
        user: User = self.request.user
        return user.favorites.all()
    
    def delete(self, request, pk):
        """
        Метод delete направлен на удаление объекта из бд. 
        Однако, так как фавориты в Django я реализовал не как 3-ю модель, а в виде обычного атрибута, 
        то я не могу указать модель и пришлось переопределит метод
        """
        user: User = request.user #Определяем авторизованного пользователя
        product = Product.objects.get(pk=pk) #Определяем продукт через pk
        user.favorites.remove(product) #Удаляем продукт из фаворитов
        return Response({"detail": "Deleted"}, status=status.HTTP_200_OK) #Возвращаем сообщение о успешном удалении и статус 200
        

