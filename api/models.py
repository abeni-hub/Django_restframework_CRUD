from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.name
    
