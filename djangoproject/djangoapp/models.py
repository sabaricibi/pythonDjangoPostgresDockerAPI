from django.db import models

# User model
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
