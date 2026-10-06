from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#
# #function based
#
# def first(request):
#     if(request.method=="GET"):
#         return HttpResponse("First page")
#
# def second(request):
#     if(request.method=="GET"):
#         return HttpResponse("Second page")



#class based

from django.views import View

class First(View):
    def get(self,request):
        return HttpResponse("First page")


class Second(View):
    def get(self, request):
        return HttpResponse("Second page")

