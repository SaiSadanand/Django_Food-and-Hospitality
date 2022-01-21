from django.db import models

# Create your models here.
class Destination(models.Model):
    
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    description=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
class Hotels(models.Model):
    
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    description=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
class Room(models.Model):
    
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    description=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
class Section(models.Model):
    
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    description=models.TextField()
    price=models.IntegerField()
    link=models.CharField(max_length=100)
class Option(models.Model):
    
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    description=models.TextField()
    price=models.IntegerField()
    link=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
class Item(models.Model):
    
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    description=models.TextField()
    price=models.IntegerField()
    link=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class Address:
    name:str
    number:str
    pincode:str
    area:str
    city:str
    state:str

    
    

