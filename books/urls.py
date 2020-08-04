from django.urls import path
from rest_framework.routers import DefaultRouter
from books import views

urlpatterns = [
    path('books/book/', views.BookViewSet.as_view({'get': 'book2'})),  # get方法用book2  后面可写post
    # path('books/banner/', views.BannerViewSet.as_view({'get': 'findBanners'}))
]

router = DefaultRouter()  # 括号不要忘了 ，不然执行不了
router.register(r"books", views.BookViewSet)

print(router.urls)
urlpatterns += router.urls
