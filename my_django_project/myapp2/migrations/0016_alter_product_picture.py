# Generated by Django 5.0.1 on 2024-02-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0015_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, default='images/default_image.jpg', upload_to=''),
        ),
    ]
