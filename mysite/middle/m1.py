#AUTHOR:FAN
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from simplejson import  *
import json

class Row1(MiddlewareMixin):
    def process_request(self,request):
        http_data={}
        f = open('file1.txt', 'w')
        for i in request.META.keys():
            http_data[i]=request.META[i]
            values=str(request.META[i])
            f.write(i+':'+values+'\n')
        f.close()
        # http=request.META
        # http_json=json.dumps(http)
        print('over')
    def process_response(self,request,response):
        print("中间件1返回")
        return response

class Row2(MiddlewareMixin):
    def process_request(self,request):
        print("中间件2请求")
        # return HttpResponse("走")
    def process_response(self,request,response):
        print("中间件2返回")
        return response

class Row3(MiddlewareMixin):
    def process_request(self,request):
        print("中间件3请求")
    def process_response(self,request,response):
        print("中间件3返回")
        return response
#
# def get_header(dict):
#