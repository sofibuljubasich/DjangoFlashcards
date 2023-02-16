from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    question = models.CharField(max_length=30)
    answer = models.CharField(max_length=180)
    category = models.CharField(max_length=30)
    known = models.BooleanField()    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question