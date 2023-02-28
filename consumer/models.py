from django.db import models
class consumer(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    phonenumber = models.PositiveBigIntegerField(null=True)
    gender = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)
    actions= models.BooleanField(default=False)

class company_Details(models.Model):
    company_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150, null=True)
    pincode = models.CharField(max_length=150, null=True)
    country = models.CharField(max_length=150, null=True)
    message= models.CharField(max_length=150, null=True)


class requirement(models.Model):
    company_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    type = models.CharField(max_length=150)
    product = models.CharField(max_length=150, null=True)
    product1 = models.CharField(max_length=150, null=True)
    product2 = models.CharField(max_length=150, null=True)
    quantatiy= models.CharField(max_length=150, null=True)
    queries = models.CharField(max_length=150, null=True)
    materails=models.CharField(max_length=150, null=True)
    b2 = models.BooleanField(default=False)