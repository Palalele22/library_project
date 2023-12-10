from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    pub_date = models.DateField()
    rented_by = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title
    
