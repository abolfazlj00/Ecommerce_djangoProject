# Generated by Django 3.2.7 on 2021-09-10 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.like'),
        ),
    ]