# Generated by Django 5.0.1 on 2024-02-22 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0020_client_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stutus',
            field=models.BooleanField(default=True),
        ),
    ]
