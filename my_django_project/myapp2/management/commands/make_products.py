from random import choice, randint, uniform


from django.core.management.base import BaseCommand, CommandParser
from myapp2.models import Product, Category


class Command(BaseCommand):
    help = "Generate fake products"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "count", type=int, help="Количество продуктов для генерации"
        )

    def handle(self, *args, **kwargs):
        catagories = Category.objects.all()
        products = []
       
        count = kwargs.get("count")
        for i in range(51, count):
            products.insert(i, Product(
                    product_name=f"product_name{i}",
                    description=f"description{i}",
                    price=uniform(0.01, 999_999.99),
                    quantity=randint(1, 10_000),
                    rating=uniform(0.01, 9.99),
                    category=choice(catagories)))
            Product.objects.bulk_create(products)
            

         
            
