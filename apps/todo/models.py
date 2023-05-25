from django.db import models
from apps.user.models import User

class Todo(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="user_todo",
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название "
    )
    description = models.TextField(
        max_length=255,
        verbose_name="Описание "
    )
    image = models.ImageField(
        upload_to="task_image",
        verbose_name="фотография",
        blank=True,null=True
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Завершено"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Таск"
        verbose_name_plural = "Таски"
        unique_together = ('user','title')