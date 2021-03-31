from django.db import models

# Create your models here.
class AddFood(models.Model):
    Food_id=models.AutoField(primary_key=True)
    Food_Type=models.CharField(max_length=100)
    Food_Name=models.CharField(max_length=100)
    Food_price=models.DecimalField(max_digits=10,decimal_places=2)
    Food_image=models.FileField(upload_to="images/")
    def __str__(self):
        return self.Food_Type
class AddNewCustomer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=200)
    customer_contact_number=models.IntegerField()
    username=models.CharField(max_length=200,default=False)
    password=models.CharField(max_length=200)
class CustomerOrder(models.Model):
    Order_id=models.AutoField(primary_key=True)
    Food_type=models.ForeignKey(AddFood,on_delete=models.CASCADE)
    Food_Name=models.CharField(max_length=500)
    Food_qty=models.CharField(max_length=500)
    Price =models.DecimalField(max_digits=12,decimal_places=2)
    Total_Amount_paid=models.DecimalField(max_digits=50,decimal_places=2,default=False)

