from django.db import models

# Create your models here.
class Data(models.Model):
    device = models.CharField(max_length=20)
    value = models.DecimalField(max_digits=8, decimal_places=4)
    
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.device}::{self.value}'