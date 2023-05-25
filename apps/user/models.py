from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        verbose_name="ваша email почта",
        unique=True
    )
    phone_number = models.CharField(
        verbose_name="ваш номер телефона",
        max_length=255
    )
    created_at = models.DateTimeField(
        verbose_name="время создание",
        auto_now_add=True
    )
    age = models.IntegerField(
        verbose_name="Возраст",
        null=True,blank=True
    )  
    def __str__(self):
        return self.username
        
    
    class Meta:
        verbose_name = "Ползователь"
        verbose_name_plural = "Ползователи"