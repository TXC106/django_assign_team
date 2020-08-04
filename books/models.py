from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField(auto_now_add=True)

    # 元类信息 : 修改表名
    class Meta:
        db_table = 'book'


# class Banner(models.Model):
#     carousel_id = models.IntegerField(auto_created=True,primary_key=True)
#     carousel_url = models.CharField(max_length=100)
#     redirect_url = models.CharField(max_length=100)
#     carousel_rank = models.IntegerField()
#     is_deleted = models.IntegerField(default=0)
#     create_time = models.DateField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'mall_carousel'
#
#
# class GoodsInfo(models.Model):
#     goods_id = models.IntegerField(auto_created=True, primary_key=True)
#     goods_name = models.CharField(max_length=200)
#     goods_intro = models.CharField(max_length=200)
#     goods_cover_img = models.CharField(max_length=200)
#     goods_carousel = models.CharField(max_length=500)
#     goods_detail_content = models.TextField()
#     original_price = models.IntegerField()
#     selling_price = models.IntegerField()
#     stock_num = models.IntegerField()
#     tag = models.CharField(max_length=20)
#     goods_sell_status = models.IntegerField()
#     create_time = models.DateField(auto_now_add=True)
#     create_user = models.IntegerField()
#     update_time = models.DateField(auto_now_add=True)
#     update_user = models.IntegerField()
#
#     class Meta:
#         db_table = 'mall_goods_info'


