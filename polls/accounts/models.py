from django.db import models

# Create your models here.
class New_User(models.Model):
    Name =models.CharField(max_length=260)
    Password=models.CharField(max_length=8)