from django.db import models


class send_mold(models.Model):
    product = models.CharField(max_length=150)
    range = models.CharField(max_length=150)
    query = models.CharField(max_length=150)
    solutionss = models.CharField(max_length=150)
    silicon_r =models.BooleanField(default=False)
