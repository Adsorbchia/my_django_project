from django.db import models
from PIL import Image
from django.shortcuts import reverse
from django.core.files.storage import FileSystemStorage



fs = FileSystemStorage(location='/media/images')




class Client(models.Model):
    username = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    user_phone = models.IntegerField()
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'username:{self.username}, surname :{self.surname}, email:{self.email}'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_of_addition = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='images/', blank=True, default='images/default_image.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)


    def __str__(self):
        return f'product_name:{self.product_name}, description :{self.description}'



class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status =  models.BooleanField(default=True)
    date_ordered = models.DateTimeField(auto_now_add=True)



    



