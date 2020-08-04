# -*- coding: utf-8 -*-
# @Time : 2020/7/23
# @Author : kiwi
# @File : serializers.py
# @Project : assign_team


from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"   # 想控制什么就写什么
        # fields = ['title']  # 只能用一个


# class BannerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Banner
#         #fields = "__all__"
#         fields = ['carousel_id','carousel_url','redirect_url','carousel_rank']
