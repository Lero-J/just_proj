from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField(max_length=255)

    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Задача'

        verbose_name_plural = 'Задачи'

        ordering = ['id']



