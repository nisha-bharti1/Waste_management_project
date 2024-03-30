from django.db import models

# Create your models here.

class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="users/image",default="")

    def __str__(self):
        return self.product_name
    

class scrap(models.Model):
    scrap_id=models.AutoField
    scrap_name=models.CharField(max_length=50)
    scrap_type=models.CharField(max_length=50,default="")
    price=models.DecimalField(max_digits=10, decimal_places=2)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="users/image",default="")

    def __str__(self):
        return self.scrap_name
