# Generated by Django 3.0.8 on 2020-08-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0025_orderinfo_order_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
