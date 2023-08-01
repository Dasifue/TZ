from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    """
    Сериализатор для регистрации пользователя
    Используются поля: username, email
    password1, password2 для проверки пароля
    """

    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def validate(self, data):
        """
        Метод validate проверяет пароли на совпадение и количество элементов в них
        """
        password1 = data.get("password1") # Из введённых данных достаём пароли
        password2 = data.get("password2")
        if len(password1) < 8: #проверяем их на длину

            #Если длина < 8, то выводится ошибка
            raise serializers.ValidationError({"password": "Password must have at least 8 characters."})
        
        if password1 != password2: #Проверка на совпадение

            #Если пароли не совпадают, то выводится ошибка
            raise serializers.ValidationError({"password":"Passwords do not match."})
        
        # Если все данные валидны, то они возвращаюстя методом
        return data
    
    def create(self, validated_data):
        """
        Метод используется для создания пользователя
        """
        user = User.objects.create( 
            username=validated_data["username"],
            email=validated_data["email"]
        ) #Выполняется queryset запрос на создание объекта в бд
        user.set_password(validated_data["password1"]) #Хешируется пароль
        user.save() #пользователь сохраняется в бд

        return user
        


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с пользователем
    """

    class Meta:
        model = User
        fields = "__all__"