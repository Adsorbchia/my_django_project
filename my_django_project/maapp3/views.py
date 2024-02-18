from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import Author, Post, Comment
from .forms import UserComment
import logging
from django.core.files.storage import FileSystemStorage



logger = logging.getLogger(__name__)


def hello(request):
    return HttpResponse('Hello world from function')

class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello world class')

def year_post(request, year):
    text =''

    return HttpResponse(f'Posts from {year}<br>{text}')


class MonthPost(View):
    def get(self, request, year, month):
        text =''
        return HttpResponse(f'Posts from {year}/{month}<br>{text}')

def post_detail(request, year, month, slug):
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создает списки в Python [] или list()",
        "content": "В процессе написания очередной программы задумался над тем кто быстрее создает списки..."
    }

    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})

def my_view(request):
    context ={'name':'John'}
    return render(request,'maapp3/my_template.html', context)


class TemplIf(TemplateView):
    template_name = 'maapp3/my_temt2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Привет Мир'
        context['number'] = 5
        return context

def veiw_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник':'оранжевый',
        'желает':'желтый',
        'знать':'зеленый',
        'где':'голубой',
        'сидит':'синий',
        'фазан':'фиолетовый',}
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'maapp3/my_temt_for.html', context)

def view_about(request):
    return render(request,'maapp3/about.html')

def view_index(request):
    return render(request, 'maapp3/index.html')


def author_post(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'maapp3/author_post.html',{'author': author, 'posts': posts})

def pull_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post).all()
    return render(request,'maapp3/post_full.html', {'post': post, 'comments': comments} )




def add_comment(request, id_post):
    if request.method == 'POST':
        form = UserComment(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            email = form.cleaned_data['email']
            post = get_object_or_404(Post, pk=id_post)
            body = form.cleaned_data['comment']
            author = Author.objects.filter(email=email).first()
            if author:
                logger.info(f'получили следующий комментарий {body=}')
                comment = Comment(author=author, post=post, body=body)
                comment.save()
                message ='Комментарий добавлен'
            else:
                name = form.cleaned_data['name']
                author = Author(name=name, email=email)
                author.save()
                comment = Comment(author=author, post=post, body=body)
                comment.save()
                logger.info(f'получили следующий комментарий {body=}')
                message ='Комментарий добавлен'
    else:
         form = UserComment()
         message ='Заполните форму' 
    return render(request, 'maapp3/comments.html', {'form':form, 'message':message})          


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
        else:
            form = ImageForm()
    return render(request, 'maapp3/upload_image.html', {'form':form})
                
            



