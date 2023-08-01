from django.urls import path

# Регистрируем все views в  endpoint'ах

from .views import (
    ProductsListApiView,
    ProductsDetailsApiView,
    FavoritesApiView,
    FavoritesDeleteApiView
)

urlpatterns = [
    path("products/list/", ProductsListApiView.as_view()),
    path("products/details/<int:pk>", ProductsDetailsApiView.as_view()),
    path("products/favorites/list", FavoritesApiView.as_view()),
    path("products/favorites/details/<int:pk>", FavoritesDeleteApiView.as_view())

]