from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.utils import json
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    @action(methods=['GET'], detail=False, url_path="banner/")
    def findBanners(self, request):
        queryset = Banner.objects.values().filter(is_deleted=0)
        # print(JsonResponse(list(queryset), safe=False))
        banner = self.get_queryset()
        print("======banner======")
        # print(queryset.data)
        if queryset != '':
        # if (len(banner) != 0):
        #     serializer = self.get_serializer(instance=banner.first())
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})


class GoodsInfoViewSet(ModelViewSet):
    queryset = GoodsInfo.objects.all()
    serializer_class = GoodsInfoSerializer

    @action(methods=['GET'], detail=False, url_path="goodsinfo/")
    def findGoodsInfo(self, request):
        queryset = GoodsInfo.objects.values().filter()
        goods_infp = self.get_queryset()
        print("======goods_info======")
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})


class UserAddressViewSet(ModelViewSet):
    queryset = GoodsInfo.objects.all()
    serializer_class = GoodsInfoSerializer

    @action(methods=['GET'], detail=False, url_path="addressList/")
    def findUserAddress(self, request):
        queryset = UserAddress.objects.values().filter()
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})

    @action(methods=['POST'], detail=False, url_path="addAddress/")
    def addUserAddress(self, request):
        # book = models.Book.objects.create(title="一本书", price=30, pub_date='2020-10-1')
        # print(book)
        # address = UserAddress.objects.create(name='name', tel='tel',
        #                            isDefault='True', province='province',
        #                            city='city', county='county',
        #                            addressDetail='addressDetail', create_time='create_time',
        #                            update_time='update_time')
        # print(address)
        # exit()
        data = json.loads(request.body)
        print("=================== address add test =====================")
        # name = request.POST['name']
        # name = request.POST.get('name')
        name = data.get('name')
        print('name:', name)
        tel = data.get('tel')
        print("==================== tel ================")
        print(tel)

        # isDefault = data.get('isDefault')
        province = data.get('province')
        city = data.get('city')
        county = data.get('county')
        addressDetail = data.get('addressDetail')
        # create_time = data.get('create_time')
        # update_time = data.get('update_time')
        # print(title, price, pubdate)
        UserAddress.objects.create(name=name, tel=tel,
                                 isDefault=False, province=province,
                                 city=city, county=county,
                                 addressDetail=addressDetail)
        return JsonResponse({'status': 200, 'message': '添加成功'})

        # return HttpResponse('添加成功')
        # return redirect('/books/list/')

    @action(methods=['POST'], detail=False, url_path="editAddress/")
    def editUserAddress(self, request):
        data = json.loads(request.body)
        address_id = data.get('address_id')
        name = data.get('name')
        tel = data.get('tel')
        # isDefault = data.get('isDefault')
        province = data.get('province')
        city = data.get('city')
        county = data.get('county')
        addressDetail = data.get('addressDetail')
        update_time = timezone.now()
        newAd = UserAddress.objects.filter(pk=address_id)
        # print(newAd.exists())
        if newAd.exists():
            UserAddress.objects.filter(pk=address_id).update(name=name, tel=tel,
                                       isDefault=False, province=province,
                                       city=city, county=county,
                                       addressDetail=addressDetail, update_time=update_time)
            return JsonResponse({'status': 200, 'message': '修改成功'})
        else:
            return JsonResponse({'status': 500, 'message': '修改失败，可能没有该id'})

    @action(methods=['POST'], detail=False, url_path="delAddress/")
    def delUserAddress(self, request):
        data = json.loads(request.body)
        address_id = data.get('address_id')
        is_deleted = True
        newAd = UserAddress.objects.filter(pk=address_id)
        # print(newAd.exists())
        if newAd.exists():
            UserAddress.objects.filter(pk=address_id).update(is_deleted=is_deleted)
            return JsonResponse({'status': 200, 'message': '删除成功'})
        else:
            return JsonResponse({'status': 500, 'message': '删除失败，可能没有该id'})

    @action(methods=['POST'], detail=False, url_path="defAddress/")
    def defUserAddress(self, request):
        data = json.loads(request.body)
        address_id = data.get('address_id')
        # for address in UserAddress.objects.all():
        #     print(address)
        #     if address == UserAddress.objects.filter(pk=address_id):
        #         address.update(isDefault=True)
        #     else:
        #         address.update(isDefault=False)
        # isDefault = True
        newAd = UserAddress.objects.filter(pk=address_id)
        # print(newAd.exists())
        if newAd.exists():
            UserAddress.objects.all().update(isDefault=False)
            newAd.update(isDefault=True)
            return JsonResponse({'status': 200, 'message': '设置默认成功'})
        else:
            return JsonResponse({'status': 500, 'message': '设置默认失败，可能没有该id'})


