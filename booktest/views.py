from django.shortcuts import render
from booktest.models import BookInfo, HeroInfo
from django.views import View
from datetime import date
from django import http
# Create your views here.

class BookInsert(View):

    def get(self,request):

        # 你这样就是创建了一个实例对象， 不能直接把这个对象传给 hbook， 因为没保存
        # book = BookInfo(
        #     btitle='西游记',
        #     bpub_date=date(1988, 1, 1),
        #     bread=10,
        #     bcomment=10
        # )
        # book = BookInfo.objects.get(id=2)
        # book.btitle = '射雕英雄传'
        # book.bpub_date = '1980-5-1'
        # book.bread = 12
        # book.bcomment = 34

        # print(book,type(book))
        # 这个才是从数据库中查询出来的对象，才可以传给 hbook，作为外键关联对象
        # book = BookInfo.objects.filter(id__exact=1)[0]

        # 也可以这样使用, 直接获取的就是对象
        book = BookInfo.objects.get(id=1)
        heros = book.heroinfo_set.all()






        return http.HttpResponse('成功')

