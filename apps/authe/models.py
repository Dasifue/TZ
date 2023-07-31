from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField("Avatar", upload_to="media/uploads/avatars/", default="media/default/avatar.png")
    phone = models.CharField("Phone", max_length=20)    
    date_updated = models.DateTimeField("Date updated", auto_now=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
    
    