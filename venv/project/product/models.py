from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.ImageField(upload_to='images/')
    category=models.CharField(max_length=20)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'المنتجات'
        ordering = ['name']
class Test(models.Model):
    Date=models.DateField()
    time=models.TimeField(null=True)
    created=models.DateTimeField(default=datetime.now)