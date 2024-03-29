# Generated by Django 5.0.1 on 2024-02-18 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.image'),
        ),
    ]
