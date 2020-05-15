from django.urls import path,re_path
from . import views

urlpatterns = [
    # 测试提取查询字符串参数：http://127.0.0.1:8000/querystring/?name=zxc&age=18
    path('querystring/', views.QSParamView.as_view()),
    path('formdata/', views.FormDataParamView.as_view()),
    path('json/', views.JSONParamView.as_view()),
    re_path(r'^url_param3/(?P<phone_nu3m>1[3-9]\d{9})/$', views.URLParam3View.as_view()),
    path('json_resp',views.JSONResponseView.as_view()),
    path('index/',views.IndexView.as_view(),name='index'),
    path('/',views.IndexView.as_view()),
    path('login_redirect/',views.LoginRedirectView.as_view()),
]