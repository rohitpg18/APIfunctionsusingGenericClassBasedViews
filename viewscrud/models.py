from django.db import models

# Create your models here.
class Emp(models.Model):
    emp_id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    department=models.CharField(max_length=10)
    
    def __str__(self):
        return self.name