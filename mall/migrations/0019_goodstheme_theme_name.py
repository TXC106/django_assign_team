# Generated by Django 3.0.8 on 2020-08-04 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0018_auto_20200804_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodstheme',
            name='theme_name',
            field=models.CharField(default='大扫除', max_length=200),
            preserve_default=False,
        ),
    ]
