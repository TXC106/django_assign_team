# Generated by Django 3.0.8 on 2020-08-04 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0015_auto_20200804_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsinfo',
            name='selling_num',
        ),
    ]
