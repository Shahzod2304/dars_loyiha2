from django.db import models

# Create your models here.
class Cafe_Name(models.Model):
    name = models.CharField(max_length=30)
    shior = models.CharField(max_length=55)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    coffee_name = models.CharField(max_length=25)
    s_price = models.PositiveIntegerField()
    l_price = models.PositiveIntegerField()
    img = models.ImageField(upload_to='images/menu')

    def __str__(self):
        return self.coffee_name
    
class About_Cafe(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.title
    


class Contact_us(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
    
