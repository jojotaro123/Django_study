from django.urls import path
from . import views

urlpatterns = [
    # 函数视图路由语法：
    # path('网络地址正则表达式', 函数视图名),

    # 用户注册：http://127.0.0.1:8000/users/register/
    path('users/register/', views.Registerview.as_view()),

]