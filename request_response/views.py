from django.shortcuts import render,redirect,reverse
from django import http
from django.views import View
import json


# Create your views here.

class QSParamView(View):

    def get(self, request):
        name = request.GET.get('name', '小明')
        age = request.GET.get('age', '0')

        response = http.HttpResponse('查询字符串参数：%s--%s' % (name, age))

        return response
    #
    # def post(self,request):
    #     name = request.GET.get('name','小明')
    #     age = request.GET.get('age','0')
    #     response = http.HttpResponse('查询字符串参数：%s--%s' % (name, age))
    #
    #     return response


class FormDataParamView(View):
    def post(self,request):

        username =  request.POST.get('username')
        password = request.POST.get('password')

        response = http.HttpResponse('表单类型参数%s--%s'% (username,password))

        return response

class JSONParamView(View):

    def post(self,request):
        json_str = request.body

        json_dict = json.loads(json_str)

        username = json_dict.get('username')
        password = json_dict.get('password')

        response = http.HttpResponse('json类型参数 %s---%s'%(username,password))
        return response

class URLParam2View(View):
    def get(self,request,phone_num):

        response = http.HttpResponse('re_path()提取路径参数: %s'%phone_num)
        print(phone_num)


        return response


class JSONResponseView(View):

    def get(self,request):

        dict_data ={
            "city" : "beijing",
            "subject" : "python"

        }

        return http.JsonResponse(dict_data)

class IndexView(View):

    def get(self,request):


        return http.HttpResponse('首页')


class LoginRedirectView(View):


    def post(self,request):

        ret_url = reverse('request_response:index')

        return redirect(ret_url)

