# Generated by Django 3.0.8 on 2020-08-03 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_goodsinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.DeleteModel(
            name='GoodsInfo',
        ),
    ]