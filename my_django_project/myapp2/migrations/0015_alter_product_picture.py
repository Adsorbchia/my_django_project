# Generated by Django 5.0.1 on 2024-02-21 06:51

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0014_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, default='images/default_image.jpg', storage=django.core.files.storage.FileSystemStorage(location='/media/images'), upload_to=''),
        ),
    ]