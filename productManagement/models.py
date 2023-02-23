from djongo import models

# Create your models here.


class Products(models.Model):
    codProduct=models.ObjectIdField
    name=models.CharField(max_length=50)
    productCategory=models.ForeignKey()
    
 
    