from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
