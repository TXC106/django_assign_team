import random

from django.db import models


class Banner(models.Model):
    carousel_id = models.IntegerField(auto_created=True,primary_key=True)
    carousel_url = models.CharField(max_length=100)
    redirect_url = models.CharField(max_length=100)
    carousel_rank = models.IntegerField()
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'mall_carousel'


class GoodsInfo(models.Model):
    goods_id = models.IntegerField(auto_created=True, primary_key=True)
    goods_name = models.CharField(max_length=200)
    goods_intro = models.CharField(max_length=200)
    goods_category_id = models.IntegerField(default=0)
    goods_cover_img = models.CharField(max_length=200)
    goods_carousel = models.CharField(max_length=500)
    goods_detail_content = models.TextField()
    original_price = models.IntegerField()
    selling_price = models.IntegerField()
    stock_num = models.IntegerField()
    tag = models.CharField(max_length=20)
    goods_sell_status = models.IntegerField()
    create_user = models.IntegerField()
    create_time = models.DateField(auto_now_add=True)
    update_user = models.IntegerField()
    update_time = models.DateField(auto_now_add=True)
    selling_num = models.IntegerField(default=0)
    goods_theme_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'goods_info'


# class UserAddress(models.Model):
#     address_id = models.IntegerField(auto_created=True, primary_key=True)
#     user_name = models.CharField(max_length=200)
#     user_phone = models.CharField(max_length=20)
#     default_flag = models.IntegerField()
#     province_name = models.CharField(max_length=200)
#     city_name = models.CharField(max_length=200)
#     region_name = models.CharField(max_length=200)
#     detail_address = models.CharField(max_length=200)
#     create_time = models.DateField(auto_now_add=True)
#     update_time = models.DateField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'user_address'

class UserInfo(models.Model):
    user_id = models.IntegerField(auto_created=True, primary_key=True)
    login_name = models.CharField(max_length=200)
    user_pwd = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=200)
    introduce = models.CharField(max_length=500)
    locked = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'mall_user'


class UserAddress(models.Model):
    address_id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=20)
    isDefault = models.BooleanField(default=False)
    country = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    id = models.CharField(max_length=200)
    addressDetail = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    areaCode = models.CharField(max_length=200)
    postalCode = models.CharField(max_length=200)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_address'


class UserToken(models.Model):
    user_id = models.IntegerField(auto_created=True, primary_key=True)
    token = models.CharField(max_length=500)
    update_time = models.DateField(auto_now_add=True)
    expire_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'user_token'


class GoodsCategory(models.Model):
    category_id = models.IntegerField(auto_created=True, primary_key=True)
    category_level = models.IntegerField(default=0)
    parent_id = models.IntegerField(default=0)
    category_name = models.CharField(max_length=200)
    category_rank = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True)
    create_user = models.IntegerField(default=0)
    update_time = models.DateField(auto_now_add=True)
    update_user = models.IntegerField(default=0)
    carousel_1 = models.CharField(max_length=200, default=None)
    carousel_2 = models.CharField(max_length=200, default=None)
    carousel_small = models.CharField(max_length=200, default=None)

    class Meta:
        db_table = 'goods_category'


class ShoppingCart(models.Model):
    cart_item_id = models.IntegerField(auto_created=True, primary_key=True)
    goods_count = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now_add=True)
    user_id = models.IntegerField(default=0)
    goods_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'shopping_cart'


class OrderInfo(models.Model):
    order_id = models.IntegerField(auto_created=True, primary_key=True)
    user_id = models.IntegerField(default=0)
    order_no = models.IntegerField()
    total_price = models.IntegerField(default=1)
    pay_status = models.IntegerField(default=0)
    pay_type = models.CharField(max_length=20)
    pay_time = models.DateField()
    order_status = models.IntegerField(default=0)
    extra_info = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'mall_order'


class OrderItem(models.Model):
    order_item_id = models.IntegerField(auto_created=True, primary_key=True)
    user_id = models.IntegerField(default=0)
    order_id = models.IntegerField(default=0)
    cart_item_id = models.IntegerField(default=0)
    goods_cover_img = models.CharField(max_length=200)
    selling_price = models.IntegerField(default=1)
    goods_count = models.IntegerField()
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'order_item'


class GoodsTheme(models.Model):
    theme_id = models.IntegerField(auto_created=True, primary_key=True)
    theme_name = models.CharField(max_length=200)
    theme_pic = models.CharField(max_length=200)
    theme_pic_small = models.CharField(max_length=200)

    class Meta:
        db_table = 'goods_theme'
