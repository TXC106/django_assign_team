from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(methods=['GET'], detail=False, url_path='book/')
    def book2(self, request):
        # book = self.get_queryset().filter(title=name)
        book = self.get_queryset()
        print("===========book===========")
        if(len(book) == 0):
            return JsonResponse({'status': 0, 'msg': '用户名不存在'})
        else:
            serializer = self.get_serializer(instance=book.first())
            return JsonResponse({'status': 1, 'msg': '用户名已存在', 'data': serializer.data})
            # return JsonResponse({'status': 1, 'msg': '用户名已存在'})


# class BannerViewSet(ModelViewSet):
#     queryset = Banner.objects.all()
#     serializer_class = BannerSerializer
#
#     @action(methods=['GET'], detail=False, url_path="banner/")
#     def findBanners(self, request):
#         queryset = Banner.objects.values().filter(is_deleted=0)
#         # print(JsonResponse(list(queryset), safe=False))
#         banner = self.get_queryset()
#         print("======banner======")
#         # print(queryset.data)
#         if (queryset != ''):
#         # if (len(banner) != 0):
#         #     serializer = self.get_serializer(instance=banner.first())
#             return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
#         else:
#             return JsonResponse({'status': 500, 'message': '服务器发生错误'})
