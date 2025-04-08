from django.contrib.auth.models import User
from django.db import models


class Like(models.Model):
    answer = models.ForeignKey("Answer", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
