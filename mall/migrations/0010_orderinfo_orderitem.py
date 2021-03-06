# Generated by Django 3.0.8 on 2020-08-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0009_shoppingcart_userinfo_usertoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('order_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('order_no', models.IntegerField()),
                ('total_price', models.IntegerField(default=1)),
                ('pay_status', models.IntegerField(default=0)),
                ('pay_type', models.CharField(max_length=20)),
                ('pay_time', models.DateField()),
                ('order_status', models.IntegerField(default=0)),
                ('extra_info', models.CharField(max_length=200)),
                ('is_deleted', models.BooleanField(verbose_name=False)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'mall_order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('order_item_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=200)),
                ('goods_cover_img', models.CharField(max_length=200)),
                ('selling_price', models.IntegerField(default=1)),
                ('goods_count', models.IntegerField()),
                ('create_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'order_item',
            },
        ),
    ]
