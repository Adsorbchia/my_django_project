from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = 'Deleded product by id'


    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='deleted the product')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
        self.stdout.write(f'{product}')