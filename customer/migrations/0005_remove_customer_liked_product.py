# Generated by Django 3.2.7 on 2021-09-15 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='liked_product',
        ),
    ]
