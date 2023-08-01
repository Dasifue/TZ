from django.urls import path, include

from .views import (
    UsersListApiView,
    UserRegistrationApiView,
)

urlpatterns = [
    path("user/list/", UsersListApiView.as_view()),
    path("user/register/", UserRegistrationApiView.as_view()),
    path("user/session/", include("rest_framework.urls")),
    path("user/djoser/", include("djoser.urls.authtoken")),
]