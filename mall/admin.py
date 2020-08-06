from django.contrib import admin
from .models import *


admin.AdminSite.site_header = '移动电商管理系统'
admin.AdminSite.site_title = '移动电商管理系统'


class BannerAdmin(admin.ModelAdmin):
    list_display = ['carousel_id', 'carousel_url', 'redirect_url', 'carousel_rank', 'is_deleted', 'create_time']
    fieldsets = [
        ('轮播图URL', {'fields': ['carousel_url']}),
        ('链接地址', {'fields': ['redirect_url']}),
        ('轮播排序', {'fields': ['carousel_rank']}),
        ('是否删除', {'fields': ['is_deleted']}),
    ]
    list_per_page = 10


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['goods_id', 'goods_name', 'goods_intro', 'goods_cover_img', 'goods_carousel', 'goods_detail_content',
                    'original_price', 'selling_price', 'stock_num', 'tag', 'goods_sell_status', 'create_time',
                    'create_user', 'update_time', 'update_user', 'selling_num']
    fieldsets = [
        ('商品名称', {'fields': ['goods_name']}),
        ('商品介绍', {'fields': ['goods_intro']}),
        ('分类id', {'fields': ['good_category_id']}),
        ('商品主图', {'fields': ['goods_cover_img']}),
        ('商品轮播图', {'fields': ['goods_carousel']}),
        ('商品价格', {'fields': ['original_price']}),
        ('商品实际售价', {'fields': ['selling_price']}),
        ('商品库存数量', {'fields': ['stock_num']}),
        ('商品上架状态 1-下架 0-上架', {'fields': ['goods_sell_status']}),
        ('添加者主键id', {'fields': ['create_user']}),
        ('修改者主键id', {'fields': ['update_user']}),
        ('销售数量', {'fields': ['selling_num']}),
    ]
    list_per_page = 10


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['address_id', 'name', 'tel', 'isDefault', 'province', 'city']
    fieldsets = [
        ('收货人姓名', {'fields': ['name']}),
        ('收货人电话', {'fields': ['tel']}),
        ('是否默认地址', {'fields': ['isDefault']}),
        ('省', {'fields': ['province']}),
        ('市', {'fields': ['city']}),
        ('地区', {'fields': ['county']}),
    ]
    list_per_page = 10


admin.site.register(Banner, BannerAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
admin.site.register(GoodsCategory, CategoryAdmin)
