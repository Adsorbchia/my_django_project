from django.db import models





class Client(models.Model):
    username = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    user_phone = models.IntegerField()
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'username:{self.username}, surname :{self.surname}, email:{self.email}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_of_addition = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='images/', default='')
 

    def __str__(self):
        return f'product_name:{self.product_name}, description :{self.description}'

class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)


   


