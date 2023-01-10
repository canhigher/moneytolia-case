from django.db import models
from django.contrib.auth.models import User


class Status(models.TextChoices):
    TO_DO = 'TO DO'
    IN_PROGRESS = 'IN PROGRESS'
    DONE = 'DONE'


class Todo(models.Model):
    title = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=Status.choices, default=Status.TO_DO, max_length=20)
