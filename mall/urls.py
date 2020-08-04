from django.urls import path
from rest_framework.routers import DefaultRouter
from mall import views

urlpatterns = [
    # path('books/book/', views.BookViewSet.as_view({'get': 'book2'})),  # get方法用book2  后面可写post
    path('mall/banner/', views.BannerViewSet.as_view({'get': 'findBanners'})),
    path('mall/goodsinfo/', views.GoodsInfoViewSet.as_view({'get': 'findGoodsInfo'})),
    path('address/addressList/', views.UserAddressViewSet.as_view({'get': 'findUserAddress'})),
    path('address/addAddress/', views.UserAddressViewSet.as_view({'post': 'addUserAddress'})),
    path('address/editAddress/', views.UserAddressViewSet.as_view({'post': 'editUserAddress'})),
    path('address/delAddress/', views.UserAddressViewSet.as_view({'post': 'delUserAddress'})),
    path('address/defAddress/', views.UserAddressViewSet.as_view({'post': 'defUserAddress'})),
]

router = DefaultRouter()  # 括号不要忘了 ，不然执行不了
router.register(r"mall", views.GoodsInfoViewSet)

print(router.urls)
urlpatterns += router.urls
