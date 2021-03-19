from django.db import models
from datetime import datetime
# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(max_length=100)
    date = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name