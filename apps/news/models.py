from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Загаловак"
    )
    description = models.TextField(
        verbose_name="Описания"
    )
    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"