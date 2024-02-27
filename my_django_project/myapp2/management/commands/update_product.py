from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = 'Update product address by id '

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='product id')
        parser.add_argument('quantity', type=int, help='product quantity')



    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        quantity = kwargs['quantity']
        product = Product.objects.filter(pk=pk).first()
        product.quantity = quantity
        product.save()
        self.stdout.write(f'{product}')