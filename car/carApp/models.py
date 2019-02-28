from django.db import models

# Create your models here.

class NewCar(models.Model):
    make = models.CharField(max_length=100,default="")
    model = models.CharField(max_length=100, default="")
    year = models.IntegerField(max_length=4)
    mpg = models.DecimalField( max_digits=5, decimal_places=2)

    def __str__(self):
        return self.make