from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework import status

from .models import User

from .serializers import (
    UserRegistrationSerializer,
    UserSerializer
    )

class UsersListApiView(ListAPIView):
    """
    View выводит всех пользователей в массиве при GET запросе
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRegistrationApiView(APIView):
    """
    View направлена на регистрацию пользователя
    """
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def post(self, request): #Метод принимает POST запрос с JSON данными. Обрабатывает их и создаёт пользователя
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)