from django.shortcuts import render
from .models import  Department, Areas, Employee

def home(request):
    return render(request, 'first_app/home.html')

def about(request):
    return render(request, 'first_app/about.html')

def news(request):
    return render(request, 'first_app/news.html')


def get_dept_details(request, dept_id):
    print(" ID is ",dept_id)
    # select * from department where id = dept_id
    try:
        dept_details = Department.objects.get(pk = dept_id)
    except Exception as e:
        dept_details= None

    dept = { }
    if dept_details :
        dept['name'] = dept_details.name
        dept['description'] = dept_details.description
    else:
        dept['exception'] = f"NO Details found for id {dept_id}"
    import json
    return render(request,template_name="first_app/dept_details.html",context=dept)

def get_area_details(request,area_id):
    try:
        area_details = Areas.objects.get(pk = area_id)
    except Exception as e:
        area_details = None

    area = { }
    if area_details:
        area['areaname'] = area_details.areaname
        area['areacode'] = area_details.areacode
        area['areamember'] = area_details.areamember
    else:
        area['Exception'] = f" NO Area found with that  {area_id} Code"
    return render(request,template_name="first_app/areas.html",context=area)

def get_employee_details(request, emp_id):
    try:
        emp_details = Employee.objects.get(pk=emp_id)
    except Exception as e:
        emp_details = None

    emp = {}
    if emp_details:
        emp['name'] = emp_details.name
        emp['dob'] = emp_details.dob
        emp['salary'] = emp_details.salary
        emp['address'] = emp_details.address
        emp['date_created'] = emp_details.date_created
        emp['date_updated'] = emp_details.date_updated
        emp['department'] = emp_details.department
    else:
        emp['exception'] = f" No employee with {emp_id} id"
    return render(request,template_name="first_app/employee.html",context=emp)