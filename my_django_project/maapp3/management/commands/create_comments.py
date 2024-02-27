from random import choices
from django.core.management.base import BaseCommand
from maapp3.models import Author, Post, Comment


LOREM = " Lorem, ipsum dolor sit amet consectetur adipisicing elit. Modi, quos laboriosam quia deserunt eius accusamus quod minus exercitationem eos quam harum est officiis perspiciatis deleniti et ut odit quis nihil. Itaque repellat ratione voluptatibus aliquid minima nemo sint beatae facere, quidem tenetur saepe accusantium provident maiores tempora deleniti a dolore."

class Command(BaseCommand):
    help = "Generate fake comments to posts"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count of user')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        text = LOREM.split()
        for i in range(1, count + 1):
            author = Author.objects.filter(pk=i).first()
            post = Post.objects.filter(pk=i).first()
            for j in range(1, count + 1):
                comment = Comment(author=author, post=post,
                body=" ".join(choices(text, k=8)))
                comment.save()     