from django.db import models

# Create your models here.

class Item(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

class Employee(models.Model):
    id=  models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    company_name = models.CharField(max_length=70, blank=True)
    city = models.CharField(max_length=70, blank=True)
    state= models.CharField(max_length=70, blank=True)
    zip=  models.IntegerField(blank=True)
    email=  models.EmailField()   
    web= models.CharField(max_length=100, blank=True)
    age=  models.IntegerField(blank=True)
     





