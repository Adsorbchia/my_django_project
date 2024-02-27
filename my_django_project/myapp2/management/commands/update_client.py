from django.core.management.base import BaseCommand
from myapp2.models import Client


class Command(BaseCommand):
    help = 'Update client address by id '

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='client id')
        parser.add_argument('address', type=str, help='client address')



    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        address = kwargs['address']
        client = Client.objects.filter(pk=pk).first()
        client.address = address
        client.save()
        self.stdout.write(f'{client}')
