# Generated by Django 5.0.1 on 2024-02-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0016_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, default='images/default_image.jpg', upload_to='images/'),
        ),
    ]
