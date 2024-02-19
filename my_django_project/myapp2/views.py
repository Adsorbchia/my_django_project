from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Client, Product, Order
from datetime import datetime, date, time, timedelta
from django.utils import timezone 
import logging
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm

logger = logging.getLogger(__name__)




def full_orders(request, client_id):
    '''
    Выводит всесь список заказанных  пользователем товаров за все время использования магазина

    '''
    client_orders = set()
    client = get_object_or_404(Client, pk=client_id)
    for order in  Order.objects.filter(customer=client).all().iterator():
        product = order.products.all()
        for item in product:
            if item.id is not client_orders:
                client_orders.add(item.product_name)
    return render(request,'myapp2/list_orders.html', {'client': client,'client_orders': client_orders })


def full_orders_month_year_day(request, client_id, year, month, day_start, day_end):
    '''
    Выводит весь список заказанных  пользователем товаров за определенный период день/неделю/месяц
    '''
    date_start = datetime.combine(date(year, month, day_start), time.min)
    date_end = datetime.combine(date(year, month, day_end), time.max)
    client_orders = set()
    client = get_object_or_404(Client, pk=client_id)
    for order in  Order.objects.filter(date_ordered__range=(date_start, date_end)).all().iterator():
        product = order.products.all()
        for item in product:
            if item.id is not client_orders:
                client_orders.add(item.product_name)
    return render(request,'myapp2/list_orders.html', {'client': client,'client_orders': client_orders })


def full_orders_year(request, client_id, year):
    '''
    Выводит весь список заказанных пользователем товаров за конкретный год
    '''
    client_orders = set()
    client = get_object_or_404(Client, pk=client_id)
    for order in  Order.objects.filter(date_ordered__year=year).iterator():
        product = order.products.all()
        for item in product:
            if item.id is not client_orders:
                client_orders.add(item.product_name)
    return render(request,'myapp2/list_orders.html', {'client': client,'client_orders': client_orders }) 




def full_orders_day(request, client_id):
    '''
    Выводит весь список заказанных  пользователем товаров за определенный период день с учетом часового пояса
    '''
    client_orders = set()
    client = get_object_or_404(Client, pk=client_id)
    now = timezone.now()
    yesterday = now - timedelta(days=1)
    for order in  Order.objects.filter(date_ordered__range=(yesterday, now)).iterator():
        product = order.products.all()
        for item in product:
            if item.id is not client_orders:
                client_orders.add(item.product_name)
    return render(request,'myapp2/list_orders.html', {'client': client, 'client_orders': client_orders }) 




def full_orders_month(request, client_id, month, year):
    '''
     Выводит весь список заказанных пользователем товаров за определенный месяц в конкретном году
    '''
    client_orders = set()
    client = get_object_or_404(Client, pk=client_id)
    for order in  Order.objects.filter(date_ordered__year=year, date_ordered__month=month).iterator():
        product = order.products.all()
        for item in product:
            if item.id is not client_orders:
                client_orders.add(item.product_name)
    return render(request,'myapp2/list_orders.html', {'client': client,'client_orders': client_orders }) 


def upload_image(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data['picture']
            product.picture = picture.name
            product.save()
            fs = FileSystemStorage()
            fs.save(product.picture, picture)
                   
    else:
        form = ImageForm()
    return render(request, 'myapp2/upload_image_product.html', {'form':form})
