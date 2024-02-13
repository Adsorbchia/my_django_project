from django.urls import path
from .views import full_orders, full_orders_month_year_day, full_orders_day, full_orders_year, full_orders_month

urlpatterns = [
    path ('orders/<int:client_id>', full_orders, name='full_orders'),
    path('orders/<int:client_id>/<int:year>/<int:month>/<int:day_start>/<int:day_end>', full_orders_month_year_day, name='full_orders_month_year_day'),
    path('order/<int:client_id>', full_orders_day, name='full_orders_day'),
    path('orders/<int:client_id>/<int:year>/', full_orders_year, name='full_orders_year'),
    path ('orders//<int:client_id>/<int:month>/', full_orders_month, name='full_orders_month'),
]






