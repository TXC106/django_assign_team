# Generated by Django 3.0.8 on 2020-08-05 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0023_auto_20200805_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order_id',
            field=models.IntegerField(default=0),
        ),
    ]