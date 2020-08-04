# Generated by Django 3.0.8 on 2020-08-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0008_auto_20200804_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('cart_item_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('goods_count', models.IntegerField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'shopping_cart',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('login_name', models.CharField(max_length=200)),
                ('user_pwd', models.CharField(max_length=200)),
                ('nick_name', models.CharField(max_length=200)),
                ('introduce', models.CharField(max_length=500)),
                ('locked', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('create_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'mall_user',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=500)),
                ('update_time', models.DateField(auto_now_add=True)),
                ('expire_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_token',
            },
        ),
    ]
