from django.core.management.base import BaseCommand
from myapp2.models import Client, Order, Product

class Command(BaseCommand):
    help = 'Generate fake clients and products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1, count +1):
            client = Client(username=f'Username{i}', surname=f'Surname{i}', email=f'username_surmame{i}@mail.ru', user_phone=1234567+i, address=f'sity{i}, street{i},home{i}')
            client.save()
            product = Product(product_name=f'product_name{i}', description=f'description{i}', price= 10.99, quantity=i)
            product.save()

            