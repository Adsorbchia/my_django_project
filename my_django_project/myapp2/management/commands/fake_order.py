from django.core.management.base import BaseCommand
from myapp2.models import Client, Order, Product


class Command(BaseCommand):
    help = 'Generate fake orders'

    def add_arguments(self, parser):
        parser.add_argument('pk_cl', type=int)
        parser.add_argument('pk1', type=int)
        parser.add_argument('pk2', type=int)
      
    def handle(self, *args, **kwargs):
        pk_cl = kwargs['pk_cl']
        pk1 = kwargs['pk1']
        pk2 = kwargs['pk2']
        product_1 = Product.objects.filter(pk=pk1).first()
        product_2 = Product.objects.filter(pk=pk2).first()
        total_price = product_1.price + product_2.price
        client = Client.objects.filter(pk=pk_cl).first()
        order = Order(customer=client, total_price=total_price)
        order.save()
        order.products.add(product_1)
        order.products.add(product_2)
        

          