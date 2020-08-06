import time

from django.db.models import Q
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

    @action(methods=['POST'], detail=False, url_path="goodsinfobyname/")
    def findGoodsInfoByName(self, request):
        data = json.loads(request.body)
        name = data.get('goods_name')
        queryset = GoodsInfo.objects.values().filter(Q(goods_name__icontains=name))
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})

    @action(methods=['GET'], detail=False, url_path="goodsactivity/")
    def findGoodsActivityList(self, request):
        themes = list(GoodsTheme.objects.values().filter(Q(theme_pic=None)))
        data = []
        # res = {}
        for theme in themes:
            res = {}
            id = theme["theme_id"]
            # print(id)
        # exit()
            pic = theme["theme_pic_small"]
            name = theme["theme_name"]
            child = list(GoodsInfo.objects.values().filter(Q(goods_theme_id=id)))
            res.update({
                'theme_id': id,
                'theme_pic': pic,
                'theme_name': name,
                'child': child,
                        })
            data.append(res)

        if res != '':
            return JsonResponse({'status': 200, 'data': data}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})

    @action(methods=['POST'], detail=False, url_path="goodsactivitybyid/")
    def findGoodsActivityById(self, request):
        data = json.loads(request.body)
        theme_id = data.get('theme_id')
        theme = list(GoodsTheme.objects.values().filter(Q(theme_id=theme_id)))
        data = []
        res = {}
        id = theme[0]["theme_id"]
        pic = theme[0]["theme_pic"]
        name = theme[0]["theme_name"]
        child = list(GoodsInfo.objects.values().filter(Q(goods_theme_id=id)))
        res.update({
            'theme_id': id,
            'theme_pic': pic,
            'theme_name': name,
            'child': child,
                    })
        data.append(res)

        if res != '':
            return JsonResponse({'status': 200, 'data': data}, safe=False)
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

    @action(methods=['POST'], detail=False, url_path="goodinfo/")
    def findGoodInfo(self, request):
        data = json.loads(request.body)
        goods_id = data.get('goods_id')
        queryset = GoodsInfo.objects.values().filter(pk=goods_id)
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})

    @action(methods=['GET'], detail=False, url_path="goodscateory/")
    def findGoodsCategoryList(self, request):
        ctg1 = list(GoodsCategory.objects.values().filter())  # filter(Q(parent_id=0))
        # return JsonResponse({'data': list(ctg1)})
        # print(JsonResponse({'data': list(ctg1)})["data"])
        # ctg1_dict = {'data':}
        # exit()
        # 合并
        res = {}
        for ctg in ctg1:
            # v["parent_id"] = v["parent_id"] if v["parent_id"] else 0
            # 以id为key，存储当前元素数据
            res.setdefault(ctg["category_id"], ctg)
        for ctg in ctg1:
            res.setdefault(ctg["parent_id"], {}).setdefault("children", []).append(ctg)
            # 这里默认的关联关系，v的内存地址是一致的，所以后续修改只后，关联的结构也会变化。
        # print(res[0]["children"])

        if res != '':
            return JsonResponse({'status': 200, 'data': res[0]["children"]}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})
        # data = [
        #     {'id': 10, 'parent_id': 8, 'name': "ACAB"},
        #     {'id': 9, 'parent_id': 8, 'name': "ACAA"},
        #     {'id': 8, 'parent_id': 7, 'name': "ACA"},
        #     {'id': 7, 'parent_id': 1, 'name': "AC"},
        #     {'id': 6, 'parent_id': 3, 'name': "ABC"},
        #     {'id': 5, 'parent_id': 3, 'name': "ABB"},
        #     {'id': 4, 'parent_id': 3, 'name': "ABA"},
        #     {'id': 3, 'parent_id': 1, 'name': "AB"},
        #     {'id': 2, 'parent_id': 0, 'name': "AA"},
        #     {'id': 1, 'parent_id': 0, 'name': "A"},
        # ]
        #
        # def list_to_tree(data):
        #     res = {}
        #     for v in data:
        #         # v["parent_id"] = v["parent_id"] if v["parent_id"] else 0
        #         # 以id为key，存储当前元素数据
        #         res.setdefault(v["id"], v)
        #     for v in data:
        #         res.setdefault(v["parent_id"], {}).setdefault("children", []).append(v)
        #         # 这里默认的关联关系，v的内存地址是一致的，所以后续修改只后，关联的结构也会变化。
        #     return res[0]["children"]
        #
        # ret = list_to_tree(data)
        # return JsonResponse({'status': 200, 'data': ret}, safe=False)
# ===================== filter =======================

    @action(methods=['GET'], detail=False, url_path="goodsinfobyprice/")
    def findGoodsInfoByPrice(self, request):
        queryset = GoodsInfo.objects.values().order_by('-selling_price')
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})

    @action(methods=['GET'], detail=False, url_path="goodsinfobyselling/")
    def findGoodsInfoBySelling(self, request):
        queryset = GoodsInfo.objects.values().order_by('-selling_num')
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})

# ========================== 分类筛选 ================================

    @action(methods=['POST'], detail=False, url_path="goodsinfoc/")
    def findGoodsInfoC(self, request):
        data = json.loads(request.body)
        cid = data.get('goods_category_id')
        queryset = GoodsInfo.objects.values().filter(Q(goods_category_id=cid))
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})

    @action(methods=['POST'], detail=False, url_path="goodsinfocbyprice/")
    def findGoodsInfoCByPrice(self, request):
        data = json.loads(request.body)
        cid = data.get('goods_category_id')
        queryset = GoodsInfo.objects.values().filter(Q(goods_category_id=cid)).order_by('-selling_price')
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})

    @action(methods=['POST'], detail=False, url_path="goodsinfocbyselling/")
    def findGoodsInfoCBySelling(self, request):
        data = json.loads(request.body)
        cid = data.get('goods_category_id')
        queryset = GoodsInfo.objects.values().filter(Q(goods_category_id=cid)).order_by('-selling_num')
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})

# ========================= 主题查询 ============================

    @action(methods=['GET'], detail=False, url_path="goodstheme/")
    def findGoodsThemeList(self, request):
        themes = list(GoodsTheme.objects.values().filter(Q(theme_pic_small=None)))
        data = []
        # print(themes)
        # res = {}
        for theme in themes:
            # print('theme')
            # print(theme)
            res = {}
            id = theme["theme_id"]
            # print(id)
        # exit()
            pic = theme["theme_pic"]
            name = theme["theme_name"]
            child = list(GoodsInfo.objects.values().filter(Q(goods_theme_id=id)))
            res.update({
                'theme_id': id,
                'theme_pic': pic,
                'theme_name': name,
                'child': child,
                        })
            # print('res')
            # print(res)
            data.append(res)
        # print('data')
        # print(data)

        if data != []:
            return JsonResponse({'status': 200, 'data': data}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})

    @action(methods=['POST'], detail=False, url_path="goodsthemebyid/")
    def findGoodsThemeById(self, request):
        data = json.loads(request.body)
        theme_id = data.get('theme_id')
        theme = list(GoodsTheme.objects.values().filter(Q(theme_id=theme_id)))
        print(theme)
        data = []
        res = {}
        id = theme[0]["theme_id"]
        pic = theme[0]["theme_pic"]
        name = theme[0]["theme_name"]
        child = list(GoodsInfo.objects.values().filter(Q(goods_theme_id=id)))
        res.update({
            'theme_id': id,
            'theme_pic': pic,
            'theme_name': name,
            'child': child,
                    })
        data.append(res)

        if res != '':
            return JsonResponse({'status': 200, 'data': data}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})


class GoodsCartViewSet(ModelViewSet):

    @action(methods=['POST'], detail=False, url_path="goodscartbyid/")
    def findGoodsCartById(self, request):
        data = json.loads(request.body)
        user_id = data.get('user_id')
        queryset = list(ShoppingCart.objects.values().filter(Q(user_id=user_id, is_deleted=False)))
        # print(queryset)
        data = []
        money_sum = 0
        for goods in queryset:
            res = {}
            cart_item_id = goods["cart_item_id"]
            goods_id = goods["goods_id"]
            goods_count = goods["goods_count"]
            create_time = goods["create_time"]
            update_time = goods["update_time"]
            goods_info = list(GoodsInfo.objects.values().filter(Q(goods_id=goods_id)))
            # print(goods_info)
            money_sum = money_sum + goods_info[0]['selling_price']*goods_count
            res.update({
                'cart_item_id': cart_item_id,
                'goods_id': goods_id,
                'goods_count': goods_count,
                'create_time': create_time,
                'update_time': update_time,
                'goods_info': goods_info,
                        })
            data.append(res)
        if queryset != '':
            return JsonResponse({'status': 200, 'data': data, 'sum': money_sum}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})

    @action(methods=['POST'], detail=False, url_path="addcart/")
    def addUserCart(self, request):
        data = json.loads(request.body)
        user_id = data.get('user_id')
        goods_id = data.get('goods_id')
        create_time = timezone.now()
        goods_count = data.get('goods_count')
        is_deleted = False
        # checkGoods = GoodsInfo.objects.values().filter(Q(goods_id=goods_id, is_deleted=False))
        checkGoods = GoodsInfo.objects.values().filter(Q(goods_id=goods_id))
        if not checkGoods.exists():
            return JsonResponse({'status': 500, 'message': '商品不存在'})
        checkNum = ShoppingCart.objects.values().filter(Q(user_id=user_id, goods_id=goods_id, is_deleted=False))
        # print(list(checkNum))
        if checkNum.exists():
            # num = list(checkNum)[0]['goods_count']
            if goods_count == 0:
                ShoppingCart.objects.filter(Q(user_id=user_id, goods_id=goods_id)).update(is_deleted=True,
                                                                        goods_count=0, update_time=create_time)
            else:
                ShoppingCart.objects.filter(Q(user_id=user_id, goods_id=goods_id)).update(goods_count=goods_count,
                                                                                          is_deleted=False, update_time=create_time)

            # print("ok")
            # print(num)
            # ShoppingCart.objects.filter(Q(user_id=user_id, goods_id=goods_id)).update(goods_count=goods_count, is_deleted=False, update_time=create_time)
        else:
            ShoppingCart.objects.create(user_id=user_id, goods_id=goods_id,
                                 create_time=create_time, goods_count=goods_count,
                                        is_deleted=is_deleted)

        return JsonResponse({'status': 200, 'message': '添加成功'})

    # @action(methods=['POST'], detail=False, url_path="editcart/")
    # def EditUserCart(self, request):
    #     data = json.loads(request.body)
    #     user_id = data.get('user_id')
    #     goods_id = data.get('goods_id')
    #     goods_count = data.get('goods_count')
    #     update_time = timezone.now()
    #     is_deleted = False
    #     checkNum = ShoppingCart.objects.values().filter(Q(user_id=user_id, goods_id=goods_id, is_deleted=False))
    #     if checkNum.exists():
    #         if goods_count == 0:
    #             ShoppingCart.objects.filter(Q(user_id=user_id, goods_id=goods_id)).update(is_deleted=True, goods_count=0,
    #                                                                                       update_time=update_time)
    #         else:
    #             ShoppingCart.objects.filter(Q(user_id=user_id, goods_id=goods_id)).update(goods_count=goods_count, update_time=create_time)
    #     else:
    #         return JsonResponse({'status': 500, 'message': '商品不存在'})

    @action(methods=['POST'], detail=False, url_path="delcart/")
    def delUserCart(self, request):
        data = json.loads(request.body)
        # user_id = data.get('user_id')
        cart_item_id = data.get('cart_item_id')
        update_time = timezone.now()
        is_deleted = True
        for cid in cart_item_id:
            ShoppingCart.objects.filter(Q(cart_item_id=cid)).update(is_deleted=is_deleted, update_time=update_time)
        return JsonResponse({'status': 200, 'message': '删除成功'})

class OrderViewSet(ModelViewSet):

    @action(methods=['POST'], detail=False, url_path="orderbyuid/")
    def findOrderByUId(self, request):
        data = json.loads(request.body)
        user_id = data.get('user_id')
        queryset = list(OrderInfo.objects.values().filter(Q(user_id=user_id, is_deleted=False)))
        print("queryset===========================")
        print(queryset)
        orders_crete = []
        for order in queryset:
            order_dict = {}
            order_no = order["order_no"]
            total_price = order["total_price"]
            create_time = order["create_time"]
            pay_status = order["pay_status"]
            # cart_item_id = goods["cart_item_id"]
            order_info = list(OrderItem.objects.values().filter(Q(order_id=order_no)))
            # goods_info = list(ShoppingCart.objects.values().filter(Q(user_id=user_id, is_deleted=False)))
            # print(queryset)
            goods_concrete = []
            money_sum = 0
            for goods in order_info:
                goods_dict = {}
                cart_item_id = goods["cart_item_id"]
                order_id = goods["order_id"]
                # goods_id = goods["goods_id"]
                goods_counts = goods["goods_count"]
                # create_time = goods["create_time"]
                # update_time = goods["update_time"]
                carts = list(ShoppingCart.objects.values().filter(Q(cart_item_id=cart_item_id, is_deleted=False)))
                # print(queryset)
                cart_list = []
                # money_sum = 0

                goods_id = carts[0]["goods_id"]
                goods_count = carts[0]["goods_count"]
                # create_time = carts["create_time"]
                # update_time = carts["update_time"]
                goods_info = list(GoodsInfo.objects.values().filter(Q(goods_id=goods_id)))
                # print(goods_info)
                money_sum = money_sum + goods_info[0]['selling_price'] * goods_count
                goods_dict.update({
                    'cart_item_id': cart_item_id,
                    'goods_id': goods_id,
                    'goods_count': goods_count,
                    # 'create_time': create_time,
                    # 'update_time': update_time,
                    'goods_info': goods_info,
                })
                goods_concrete.append(goods_dict)
                print("goods_concrete===========================")
                print(goods_concrete)
            order_dict.update({
                'order_no': order_no,
                'total_price' : total_price,
                'create_time': create_time,
                'pay_status': pay_status,
                'order_info': goods_concrete
            })
            orders_crete.append(order_dict)
            print("orders_crete===========================")
            print(orders_crete)
        if queryset != '':
            return JsonResponse({'status': 200, 'data': orders_crete}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发生错误'})

    @action(methods=['POST'], detail=False, url_path="addorder/")
    def addUserOrder(self, request):
        data = json.loads(request.body)
        user_id = data.get('user_id')
        print("============================")
        print(user_id)
        # cart_item_id = ['1', '2']
        cart_item_id = data.get('cart_item_id')
        order_id = int(time.time())
        create_time = timezone.now()
        sum = 0
        for cid in cart_item_id:
            queryset = list(ShoppingCart.objects.values().filter(Q(cart_item_id=cid, is_deleted=False)))
        #     # print(queryset)
        #     # data = []
        #     order_id = int(time.time())
            money_sum = 0

        # for goods in queryset:
        #     res = {}
            goods_id = queryset[0]["goods_id"]
            goods_count = queryset[0]["goods_count"]
            # create_time = timezone.now()
            goods_info = list(GoodsInfo.objects.values().filter(Q(goods_id=goods_id)))
            # print(goods_info)
            money_sum = goods_info[0]['selling_price'] * goods_count
            sum = sum + money_sum
            OrderItem.objects.create(order_id=order_id, user_id=user_id, cart_item_id=cid,
                                        create_time=create_time, selling_price=money_sum,
                                     goods_count=goods_count)
        OrderInfo.objects.create(order_no=order_id, user_id=user_id, total_price=sum, create_time=create_time, pay_status=1, pay_time=create_time)

        return JsonResponse({'status': 200, 'message': '添加成功'})


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


class UserInfoViewSet(ModelViewSet):

    @action(methods=['POST'], detail=False, url_path="userinfolist/")
    def findUserInfo(self, request):
        data = json.loads(request.body)
        user_id = data.get('user_id')
        queryset = UserInfo.objects.values().filter(pk=user_id)
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '可能没有该用户'})

    @action(methods=['POST'], detail=False, url_path="usersignup/")
    def addUser(self, request):
        data = json.loads(request.body)
        login_name = data.get('login_name')
        pwd = data.get('user_pwd')
        nick_name = data.get('nick_name')
        create_time = timezone.now()

        check = UserInfo.objects.filter(Q(login_name=login_name))
        if check.exists():
            return JsonResponse({'status': 500, 'message': '已存在该用户名'})
        else:
            UserInfo.objects.create(login_name=login_name, user_pwd=pwd,
                                     nick_name=nick_name, create_time=create_time)
            return JsonResponse({'status': 200, 'message': '添加成功'})

        # return HttpResponse('添加成功')
        # return redirect('/books/list/')

    @action(methods=['POST'], detail=False, url_path="userlogin/")
    def checkUser(self, request):
        data = json.loads(request.body)
        login_name = data.get('login_name')
        pwd = data.get('user_pwd')

        check = UserInfo.objects.filter(Q(login_name=login_name, user_pwd=pwd))
        if check.exists():
            return JsonResponse({'status': 200, 'message': '登陆成功'})
        else:
            return JsonResponse({'status': 500, 'message': '不存在该用户或密码错误'})


    @action(methods=['POST'], detail=False, url_path="edituserinfo/")
    def editUserInfo(self, request):
        data = json.loads(request.body)
        user_id = data.get('user_id')
        pwd = data.get('user_pwd')
        nick_name = data.get('nick_name')
        introduce = data.get('introduce')
        checkUser = UserInfo.objects.filter(pk=user_id)
        if checkUser.exists():
            UserInfo.objects.filter(pk=user_id).update(introduce=introduce, user_pwd=pwd,
                                 nick_name=nick_name)
            return JsonResponse({'status': 200, 'message': '修改成功'})
        else:
            return JsonResponse({'status': 500, 'message': '修改失败，可能没有该用户'})

