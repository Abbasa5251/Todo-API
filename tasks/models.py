from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='name', max_length=100)
    description = models.TextField(verbose_name='description', null=True, blank=True)
    is_completed = models.BooleanField(verbose_name='is completed', default=False)
    is_deleted = models.BooleanField(verbose_name='is deleted', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    