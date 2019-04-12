from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    life_motto = models.TextField()
    
    REQUIRED_FIELDS = ['life_motto']#to propt for on createsuperuser

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
