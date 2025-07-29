from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True) 





    
    

    
    
    
    