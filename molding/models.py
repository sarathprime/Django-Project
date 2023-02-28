from django.db import models

class molding(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    phonenumber = models.PositiveBigIntegerField(null=True)
    gender = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)
    actions= models.BooleanField(default=False)

class purchase(models.Model):
    product = models.CharField(max_length=150)
    computer=models.CharField(max_length=150)
    electronics=models.CharField(max_length=150)
    ceramics=models.CharField(max_length=150)
    s=models.BooleanField(default=False)

class team_register(models.Model):
    Team = models.CharField(max_length=150)
    Email=models.CharField(max_length=150)

class product_send(models.Model):
    silicon = models.CharField(max_length=150)
    quantatiy = models.CharField(max_length=150)
    s2=models.BooleanField(default=False)