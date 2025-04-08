from django.contrib.auth.models import User
from django.db import models


class Answer(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    text = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
