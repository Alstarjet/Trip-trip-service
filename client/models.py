from django.db import models

# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.IntegerField(default=0)
    
class Auto(models.Model):
    name=models.CharField(max_length=20)
    num_seats=models.IntegerField()
    create_at=models.DateField()
    
class Seat(models.Model):
    number=models.IntegerField()
    auto_id=models.ForeignKey(Auto, on_delete=models.CASCADE)
    client_id=models.ForeignKey(Client, on_delete=models.DO_NOTHING, blank=True)

