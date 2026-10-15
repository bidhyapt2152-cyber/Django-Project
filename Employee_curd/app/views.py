
# Create your views here.

#view all records
from django.http import JsonResponse
from django.views import View
from app.models import Employee

class Employeelist(View):
    def get(self,request):

        data=list(Employee.objects.all().values())

        return JsonResponse(data,safe=False)



# creating a new record
from json import loads

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name="dispatch")

class Employeecreate(View):

    def post(self,request):

        #fetch the data from client side
        form_data=request.body  #JSON format

        #convert the JSON data into python native type
        data=loads(form_data)
        i=data['empid']
        n=data['name']
        a=data['age']
        p=data['place']
        g=data['gender']
        s=data['salary']
        d=data['designation']
        j=data['joining_date']

        print(data)

        #store the data into db table using ORM query
        s=Employee.objects.create(empid=i,name=n,age=a,place=p,gender=g,salary=s,designation=d,joining_date=j)
        s.save()


        #return Response back to client
        return JsonResponse({"message":"created"})



 # TO GET A SPECIFIC STUDENT DATA

class EmployeeDetail(View):
    def get(self,request,i):       # i stores the id value coming from client
        #code
        #reads the record matching with id from db table
        qs=Employee.objects.filter(id=i)

        # convert the data into python native
        data=list(qs.values())

        #sends the response
        return JsonResponse(data,safe=False)


# Api View for updating a record
@method_decorator(csrf_exempt,name="dispatch")

class EmployeeUpdate(View):
    def put(self,request,i):

        #Reads the record match with the id from db table
        e=Employee.objects.get(id=i)

        #Fetch data coming from client side
        form_data=request.body

        #convert data formate into python native
        data=loads(form_data)

        #update each field in db record


        e.empid= data['empid']
        e.name= data['name']
        e.age = data['age']
        e.place = data['place']
        e.gender = data['gender']
        e.salary = data['salary']
        e.designation = data['designation']
        e.joining_date = data['joining_date']

        # save the record
        e.save()

  # return the response
        return JsonResponse({"message": "Employee updated"})



# Api View for partial update of record
@method_decorator(csrf_exempt,name="dispatch")

class EmployeepartialUpdate(View):
    def patch(self,request,i):
        e=Employee.objects.get(id=i)
        form_data=request.body

        data=loads(form_data)
        print(data)

        if 'empid' in data:
            e.empid=data['empid']

        if 'name' in data:
            e.name=data['name']

        if 'age' in data:
            e.age=data['age']

        if 'place' in data:
            e.place=data['place']

        if 'gender' in data:
            e.gender=data['gender']

        if 'salary' in data:
            e.salary=data['salary']

        if 'designation' in data:
                e.designation = data['designation']

        if 'joining_date' in data:
            e.joining_date=data['joining_date']


        e.save()

        return JsonResponse({"message": "Employee partially updated"})




# Apiview for deleting a new student record
@method_decorator(csrf_exempt,name="dispatch")
class EmployeeDelete(View):
    def delete(self,request,i):
        #reads the record matching with id from db table
        e=Employee.objects.get(id=i)


        # delete the record
        e.delete()

        # sends the response
        return JsonResponse({"message":"deleted successfully"})