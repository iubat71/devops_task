

from django.db import models


# Create your models here.

class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Product_refill(models.Model):
    e_id=models.IntegerField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    quantity=models.IntegerField()
    def __str__(self):

        return self.product.name

    # def get_total(self):
       
    #     total=self.product.price *self.quantity
    #     f_total+=format(total,'0.2f')
    #     return f_total   




class Package(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    detail = models.CharField(max_length=255)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  
    def __str__(self):
        return self.name

    def get_total(self):
        
        total=self.price * self.product.quantity 
        f_total=format(total,'0.2f')
        return f_total   

class Package_refill(models.Model):
    information=(('Activated', 'Activated'),
        ('Deactivated', 'Deactivated'),)
    e_id=models.IntegerField()
    package=models.ForeignKey(Package,on_delete=models.CASCADE,null=False)
    description = models.CharField(max_length=255)
    status=models.CharField(max_length=250,choices=information,default="Deactivated")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.package.name

  


        



