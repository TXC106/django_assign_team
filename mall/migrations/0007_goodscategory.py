# Generated by Django 3.0.8 on 2020-08-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0006_auto_20200803_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('category_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('category_level', models.IntegerField(default=0)),
                ('parent_id', models.IntegerField(default=0)),
                ('category_name', models.CharField(max_length=200)),
                ('category_rank', models.IntegerField(default=0)),
                ('is_deleted', models.IntegerField(default=0)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('create_user', models.IntegerField(default=0)),
                ('update_time', models.DateField(auto_now_add=True)),
                ('update_user', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'goods_category',
            },
        ),
    ]