from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)
    UNIT_CHOICES  =[
        ('ltr' , 'Liter'),
        ('kg' , 'Kilogram'),
        ('pcs' , 'Pieces'),
    ]
    unit_of_measure = models.CharField(max_length = 10 , choices = UNIT_CHOICES)
    
    def __str__(self) -> str:
        return self.name
    