# Generated by Django 3.0.8 on 2020-08-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0011_auto_20200804_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='goods_category_id',
            field=models.IntegerField(default=0),
        ),
    ]