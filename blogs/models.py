from django.db import models
from users.models import CustomUser

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}" 
