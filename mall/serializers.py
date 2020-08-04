# -*- coding: utf-8 -*-
# @Time : 2020/7/23
# @Author : kiwi
# @File : serializers.py
# @Project : assign_team


from rest_framework import serializers
from .models import *


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        #fields = "__all__"
        fields = ['carousel_id', 'carousel_url', 'redirect_url', 'carousel_rank']


class GoodsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsInfo
        #fields = "__all__"
        fields = ['goods_id', 'goods_name', 'goods_intro', 'goods_cover_img', 'goods_carousel']
