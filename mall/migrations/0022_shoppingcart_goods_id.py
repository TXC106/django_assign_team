# Generated by Django 3.0.8 on 2020-08-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0021_shoppingcart_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='goods_id',
            field=models.IntegerField(default=0),
        ),
    ]
