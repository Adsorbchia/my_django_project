from django.core.management.base import BaseCommand
from myapp2.models import Client


class Command(BaseCommand):
    help = "Create client."


    def handle(self, *args, **kwargs):
        client = Client(username="Petr",surname= "Ivanov", email="Petr@mail.ru", user_phone=7895032,address="gggdddlllnbvc iiiifffgbmn iiiyyeexx")
        client.save()
        self.stdout.write(f'{client}')

