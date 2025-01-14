from django.db import models

# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.IntegerField(default=0)

