from django.shortcuts import render
from django import http
from django.views import View

# Create your views here.

class Registerview(View):

    def get(self,request):

        return http.HttpResponse('get Response')


    def post(self,request):

        return http.HttpResponse('post regist logic')


