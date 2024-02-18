from random import choices
from django.core.management.base import BaseCommand
from maapp3.models import Author, Post

LOREM = " Lorem, ipsum dolor sit amet consectetur adipisicing elit. Modi, quos laboriosam quia deserunt eius accusamus quod minus exercitationem eos quam harum est officiis perspiciatis deleniti et ut odit quis nihil. Itaque repellat ratione voluptatibus aliquid minima nemo sint beatae facere, quidem tenetur saepe accusantium provident maiores tempora deleniti a dolore."


class Command(BaseCommand):
    help = "Generate fake authors and posts"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count of user')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        text = LOREM.split()
        for i in range(1, count + 1):
            author = Author(name=f'Author{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(title=f'title{j}',
                content=" ".join(choices(text, k=20)),
                author=author)
                post.save()
