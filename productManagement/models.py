from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='productImages', default='productImages/default.png')
    description = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name
    
    
class Offer(models.Model):
    
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    discount = models.IntegerField()
    
    def __str__(self):
        return self.code
    