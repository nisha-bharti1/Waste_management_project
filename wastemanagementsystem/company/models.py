from django.db import models

# Create your models here.

class company(models.Model):
    company_id=models.AutoField
    company_name=models.CharField(max_length=50)
    company_email=models.CharField(max_length=300)
    create_company_name=models.CharField(max_length=50)
    create_password=models.CharField(max_length=8)
    confirm_password=models.CharField(max_length=8)
    
    def __str__(self):
       return self.create_company_name

    