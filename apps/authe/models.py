from django.db import models
from django.contrib.auth.models import AbstractUser

from ..posts.models import Product


class User(AbstractUser):

    """
    Переопределяем класс User
    """

    image = models.ImageField("Avatar", upload_to="media/uploads/avatars/", default="media/default/avatar.png") #Аватар пользователя. Загружается в media. Также указывается дефолтная аватарка
    email = models.EmailField("Email address", unique=True, null=True) #Почта пользователя, переопределил атрибут для указания параметра unique
    phone = models.CharField("Phone number", max_length=20, null=True) #Номер телефона
    address = models.CharField("Address", max_length=255, null=True) #Адресс пользователя
    favorites = models.ManyToManyField(Product, related_name="users") #Фавориты постов. Реализованы через поле ManyToMany. Я не стал реализовывать ManyToMany через отдельную модель, так как не было необходимости указывать в ней сторонние атрибуты 

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        """
        Метод проперти для вывода ФИ пользователя
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()