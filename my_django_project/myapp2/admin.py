from django.contrib import admin
from .models import Product, Category, Client, Order


@admin.action(description='Сбросить количество в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

@admin.action(description='Сделать пользователя неактивным')
def inactive_client(modeladmin, request, queryset):
    queryset.update(is_active=False)



class ClientAdmin(admin.ModelAdmin):
     """Список клиентов."""
     list_display = ['username', 'surname', 'registration_date','is_active' ]
     ordering = ['username']
     list_filter = ['registration_date']
     search_fields = ['email','user_phone' ]
     search_help_text = 'Поиск по полям имя и электронный адрес'
     actions = [inactive_client]

     """ Отдельный пользователь. """

     readonly_fields =['registration_date']
     fieldsets =[( None, {
        'classes': ['wide'],
        'fields': ['username','surname'],},),
        ('Подробности',{'classes': ['collapse'],
        'description': 'Информация о клиенте', 
        'fields': ['email','user_phone'],}),]



class ProductAdmin(admin.ModelAdmin):
    
    """Список продуктов."""
    list_display = ['product_name', 'quantity', 'price', 'category']
    ordering = ['category','-quantity' ]
    list_filter = ['date_of_addition', 'price']
    search_fields = [ 'description']
    search_help_text = 'Поиск по полю описание продукта  "description" '
    actions = [reset_quantity]

    """ Отдельный продукт. """
    # fields = ['product_name', 'description', 'category','date_of_addition', 'rating' ]
    readonly_fields =['date_of_addition', 'rating' ]
    fieldsets =[( None, {
        'classes': ['wide'],
        'fields': ['product_name'],},),
        ('Подробности',{'classes': ['collapse'],
        'description': 'Категория товара и его подробное описание', 
        'fields': ['description','category'],},),
        ('Бухгалтерия',{'fields': ['quantity', 'price'],},),
        ('Рейтинг и прочее',{'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
         'fields': ['rating', 'date_of_addition'],}),]


class OrderAdmin(admin.ModelAdmin):
    """Список закзов."""
    list_display = ['date_ordered', 'total_price', 'status']
    ordering = ['total_price' ]
    list_filter = ['date_ordered']
    search_fields = ['customer' ]
    search_help_text = 'Поиск по полю покупатель "customer"'
    """ Отдельный заказ. """
    fields = ['customer', 'products','date_ordered', 'status' ]
    readonly_fields =['date_ordered' ]
      
    



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)