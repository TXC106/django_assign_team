from django.urls import path
from rest_framework.routers import DefaultRouter
from mall import views

urlpatterns = [
    # ======================= 首页 =============================

    # path('books/book/', views.BookViewSet.as_view({'get': 'book2'})),  # get方法用book2  后面可写post
    path('mall/banner/', views.BannerViewSet.as_view({'get': 'findBanners'})),

    path('mall/goodsactivity/', views.BannerViewSet.as_view({'get': 'findGoodsActivityList'})),
    path('mall/goodsactivitybyid/', views.BannerViewSet.as_view({'post': 'findGoodsActivityById'})),

    path('mall/goodsinfobyname/', views.BannerViewSet.as_view({'post': 'findGoodsInfoByName'})),

    # ======================= 商品 =============================

    path('mall/goodsinfo/', views.GoodsInfoViewSet.as_view({'get': 'findGoodsInfo'})),
    path('mall/goodscateory/', views.GoodsInfoViewSet.as_view({'get': 'findGoodsCategoryList'})),
    path('mall/goodsinfobyprice/', views.GoodsInfoViewSet.as_view({'get': 'findGoodsInfoByPrice'})),
    path('mall/goodsinfobyselling/', views.GoodsInfoViewSet.as_view({'get': 'findGoodsInfoBySelling'})),

    path('mall/goodsinfoc/', views.GoodsInfoViewSet.as_view({'post': 'findGoodsInfoC'})),
    path('mall/goodsinfocbyprice/', views.GoodsInfoViewSet.as_view({'post': 'findGoodsInfoCByPrice'})),
    path('mall/goodsinfocbyselling/', views.GoodsInfoViewSet.as_view({'post': 'findGoodsInfoCBySelling'})),

    path('mall/goodstheme/', views.GoodsInfoViewSet.as_view({'get': 'findGoodsThemeList'})),
    path('mall/goodsthemebyid/', views.GoodsInfoViewSet.as_view({'post': 'findGoodsThemeById'})),

    path('mall/goodinfo/', views.GoodsInfoViewSet.as_view({'post': 'findGoodInfo'})),

    # ======================= 地址 =============================

    path('address/addressList/', views.UserAddressViewSet.as_view({'get': 'findUserAddress'})),
    path('address/addAddress/', views.UserAddressViewSet.as_view({'post': 'addUserAddress'})),
    path('address/editAddress/', views.UserAddressViewSet.as_view({'post': 'editUserAddress'})),
    path('address/delAddress/', views.UserAddressViewSet.as_view({'post': 'delUserAddress'})),
    path('address/defAddress/', views.UserAddressViewSet.as_view({'post': 'defUserAddress'})),

    # ======================= 用户 =============================

    path('user/userinfolist/', views.UserInfoViewSet.as_view({'post': 'findUserInfo'})),
    path('user/usersignup/', views.UserInfoViewSet.as_view({'post': 'addUser'})),
    path('user/edituserinfo/', views.UserInfoViewSet.as_view({'post': 'editUserInfo'})),
    path('user/userlogin/', views.UserInfoViewSet.as_view({'post': 'checkUser'})),

    # ======================= 购物车 =============================

    path('cart/goodscartbyid/', views.GoodsCartViewSet.as_view({'post': 'findGoodsCartById'})),
    path('cart/addcart/', views.GoodsCartViewSet.as_view({'post': 'addUserCart'})),
    path('cart/delcart/', views.GoodsCartViewSet.as_view({'post': 'delUserCart'})),

    # ======================= 订单 =============================

    path('cart/orderbyuid/', views.OrderViewSet.as_view({'post': 'findOrderByUId'})),
    path('cart/addorder/', views.OrderViewSet.as_view({'post': 'addUserOrder'})),

]

router = DefaultRouter()  # 括号不要忘了 ，不然执行不了
router.register(r"mall", views.GoodsInfoViewSet)

print(router.urls)
urlpatterns += router.urls
