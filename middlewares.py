from django.utils.deprecation import MiddlewareMixin

class TestMiddleWare1(MiddlewareMixin):

    def process_request(self,request):
        print('1处理请求前自动调用')

    def process_view(self,request,view_func,view_args,view_kwargs):
        print('1处理视图前自动调用')

    def process_response(self, request, response):
        """在每个响应返回给客户端之前自动调用"""
        print('1在每个响应返回给客户端之前自动调用')
        return response


class TestMiddleWare2(MiddlewareMixin):

    def process_request(self, request):
        print('2处理请求前自动调用')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('2处理视图前自动调用')

    def process_response(self, request, response):
        """在每个响应返回给客户端之前自动调用"""
        print('2在每个响应返回给客户端之前自动调用')
        return response


