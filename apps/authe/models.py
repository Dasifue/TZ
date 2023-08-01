from django.db import models
from django.contrib.auth.models import AbstractUser

from ..posts.models import Product


class User(AbstractUser):

    image = models.ImageField("Avatar", upload_to="media/uploads/avatar/", default="media/default/avatar.png")
    email = models.EmailField("Email address", unique=True, null=True)
    phone = models.CharField("Phone number", max_length=20, null=True)
    address = models.CharField("Address", max_length=255, null=True)
    posts = models.ManyToManyField(Product, related_name="users")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()