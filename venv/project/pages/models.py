from django.db import models

# Create your models here.


class Car(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.ImageField()
    category=models.CharField(max_length=20)

#one to one

class Female(models.Model):
    name_female=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name_female
class Male(models.Model):
    name_male=models.CharField(max_length=50,null=True)
    girls=models.OneToOneField(Female,on_delete=models.CASCADE)
    def __str__(self):
        return self.name_male

# one to many

class Product(models.Model):
    title=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.title

class User(models.Model):
    name=models.CharField(max_length=50,null=True)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


# many to many

class Video(models.Model):
    title=models.CharField(max_length=50,null=True)


    def __str__(self):
        return self.title

class UserName(models.Model):
    name=models.CharField(max_length=50,null=True)


    watch=models.ManyToManyField(Video)


    def __str__(self):
        return self.name


