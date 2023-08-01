from django.urls import path

from .views import (
    UsersListApiView,
    UserRegistrationApiView,
)

urlpatterns = [
    path("user/list/", UsersListApiView.as_view()),
    path("user/register/", UserRegistrationApiView.as_view())
]