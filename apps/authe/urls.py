from django.urls import path, include

from .views import (
    UsersListApiView,
    UserRegistrationApiView,
)

#Регстрируем Views в эндпоинтах

urlpatterns = [
    path("user/list/", UsersListApiView.as_view()), #Список пользователей
    path("user/register/", UserRegistrationApiView.as_view()), #Регистрация пользователя
    path("user/session/", include("rest_framework.urls")), #Login & logout с использованием сессий
    path("user/djoser/", include("djoser.urls.authtoken")), #Login & logout с использованием токена
]