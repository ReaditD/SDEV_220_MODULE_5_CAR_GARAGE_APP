from django.db import models

# Create your models here.
class Car(models.Model):
    FUEL_TYPE = [
        ('gas', 'Gas'),#These items will show up in a list
        ('diesel', 'Diesel'),# How it shows to the user
        ('hybird', 'Hybrid'),
        ('lp_gas', 'LP Gas'),         
    ]
    ROOF_TYPE= [
        ('gas', 'Gas'),
        ('diesel', 'Diesel'), 
        ('hybird', 'Hybrid'),
        ('lp gas'), ('LP Gas')

    ]
    vin = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    door_numb = models.IntegerField()
    roof_type = models.CharField(max_length=50)
    year = models. SmallIntegerField()
    fuel_type = models.CharField(choices=FUEL_TYPE, default='gas')
    #The 'choices above is a built-in function
    def __str__(self):
        return f"{self.color} {self.model}"
    