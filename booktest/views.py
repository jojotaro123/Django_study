from django.shortcuts import render
from booktest.models import BookInfo, HeroInfo
from django.views import View
from datetime import date
from django import http
from django.db.models import F, Q, Sum


# Create your views here.

class BookInsert(View):

    def get(self, request):
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
        # book = BookInfo.objects.get(id=1)
        # hero = book.heroinfo_set.all()
        # print(hero)

        # 查询未被逻辑删除的记录
        # book = BookInfo.objects.filter(is_delete=False)
        # print(book.count())

        # 查询书名包含湖的
        # book = BookInfo.objects.filter(btitle__contains='湖')
        # print(book)

        # 查询书名不为空的书籍
        # book = BookInfo.objects.filter(btitle__isnull=False)
        # print(book)

        # 查询书籍范围1，3，5
        # book = BookInfo.objects.filter(id__in=[1,3,5])
        # print(book)

        # 查询阅读量大于评论量
        # book = BookInfo.objects.filter(bread__gt=F('bcomment'))
        # print(book)

        # 逻辑或
        # book = BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))
        # print(book)

        # 聚合
        # count = BookInfo.objects.aggregate(Sum('bread'))
        # print(count.get('bread__sum'))

        # 排序
        # book = BookInfo.objects.filter(btitle__isnull=False).order_by('bread')
        # print(book)

        # 关联查询 多查一
        # hero = HeroInfo.objects.filter(hname__contains='黄')
        # print(hero)
        # book = hero.hbook
        # print(book)
        # print(book)

        # 修改
        # HeroInfo.objects.filter(hname='孙悟空').update(hname='悟空')

        # 查all()
        #
        # heros = HeroInfo.objects.all()
        # print(heros)
        #
        # 作业1
        # book = BookInfo.objects.filter(btitle='天龙八部')
        # book_name = book[0]
        # print(book_name.bread)
        # print(book,type(book),'\r\n',book_name,type(book_name))

        # 作业2
        # book = BookInfo.objects.filter(btitle__contains='湖')
        # print(book)

        # 查询书名以'部'结尾的书籍 (模糊查询) (endswith、startswith)

        # book = BookInfo.objects.filter(btitle__endswith='部')
        # print(book)

        # 查询书名不为空的书籍(空查询)
        # book = BookInfo.objects.filter(btitle__isnull=False)
        # print(book)

        # book = BookInfo.objects.filter(id__in=[1,3,5])
        # print(book)

        # 查询编号大于3的书籍(比较查询)
        # book = BookInfo.objects.filter(id__gt=3)
        # print(book)

        # 查询id不等于3的书籍(不相等)
        #
        # book = BookInfo.objects.exclude(id=3)
        # print(book)

        # 查询1980年发表的书籍

        # book = BookInfo.objects.filter(bpub_date__year=1980)
        # print(book)

        # 查询1990年1月1日后发表的书籍

        # book = BookInfo.objects.filter(bpub_date__gte=date(1990,1,1))
        # print(book)

        # 查询阅读量大于评论量的书籍

        # book = BookInfo.objects.filter(bread__gt=F('bcomment'))
        # print(book)

        # 查询阅读量大于20，或编号小于3的图书

        # book = BookInfo.objects.filter(Q(bread__gt=20)|Q(id__lt=3))
        # print(book)

        # 查询编号为1的英雄出自的书籍

        # hero = HeroInfo.objects.get(id=1)
        # print(hero.hbook)

        # 一查多：查询编号为1的图书中所有人物信息
        # book = BookInfo.objects.get(id=1)
        # heros = book.heroinfo_set.all()
        # print(heros)
        cookie1 = request.COOKIES
        print(cookie1)

        return http.HttpResponse('成功')


class JinYong(View):

    def get(self, request):
        heros = HeroInfo.objects.all()

        context = {

            'heros': heros,
            'books': [book.hbook for book in heros]

        }
        print(context['books'])
        cookie1 = request.COOKIES.get('jojo')
        print(cookie1)

        response = render(request, 'jinyong.html', context)
        response.set_cookie('jojo', 'dio', max_age=3600)

        # 设置session
        request.session['username'] = 'jojo'

        return response
