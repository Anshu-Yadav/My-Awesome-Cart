from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=60)
    category = models.CharField(max_length=80, default="")
    subcategory = models.CharField(max_length=90, default="")
    price = models.CharField(max_length=100000000000000000,default="1,000")
    
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name



class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=300)
    Phone = models.IntegerField()
    Message = models.CharField(max_length=500)

    def __str__(self):
        return self.Name
    

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    pin_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=120, default="")

    def __str__(self):
        return self.name
    

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    