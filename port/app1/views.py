from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View

class About(View):
    def get(self,request):

        data={"id":"101","full name":"Bidhya PT","title":"Python Developer","DOB":"06-03-2002",
              "email":"www.bidhyapt22@gmail.com","contact":967535469,"location":"Kottayam",
              "github_url": "https://github.com/","linkedin_url": "https://linkedin.com/"}

        return JsonResponse(data)

class Education(View):
    def get(self,request):

        data={"id":"101","institution":"CEP","course":"ECE","university":"APJ Abdul Kalam Technological University",
              "location":"Kottayam","start year":2020,"End Year":2024,
              "grade": "A","discription": "Bachelor of Technology in Electronics and Communication Engineering"}

        return JsonResponse(data)


class Projects(View):
    def get(self,request):

        data={"id":"101","project name":"Wheelchair Safety System",
              "discription":"Multicontroller based wheelchair safety system",
              "technologies":"Python, Raspberry Pi","duration":"6 months","liveurl":"https://example.com",
              }

        return JsonResponse(data)

