from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views import View

class Studentdetails(View):
    def get(self,request):

        data={"name":"Amal","age":23,"course":"python","marks":98}

        return JsonResponse(data)



class Studentlist(View):
    def get(self,request):

        data=[
            {"name":"Anu","age":23,"course":"python","marks":87},
            {"name": "Manu", "age": 22, "course": "Data sceince", "marks": 80},
            {"name": "Athira", "age": 25, "course": "Java", "marks": 76},
            {"name": "Krishna", "age": 21, "course": "python", "marks": 91},

        ]

        return JsonResponse(data,safe=False)   #safe=False, data is given in list formate



