from django.db import models

class society(models.Model):
    society_name=models.CharField(max_length=200)
    no_of_flats=models.PositiveIntegerField()
    builder=models.CharField(max_length=200)
    address=models.CharField(max_length=250)
    area=models.CharField(max_length=250)
    city=models.CharField(max_length=100)
    constructed_on=models.DateField(auto_now=False, auto_now_add=False)
    maintenance_rating=models.IntegerField()
    