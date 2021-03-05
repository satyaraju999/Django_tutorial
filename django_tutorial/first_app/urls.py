from django.urls import path
from .views import home
from .views import about, news, get_dept_details, get_area_details, get_employee_details

urlpatterns = [
    path('home/', home ,name= 'home'),
    path('about/', about, name='about'),
    path('news/', news),
    path("departments/<int:dept_id>/",get_dept_details),
    path("areas/<int:area_id>/", get_area_details),
    path("employee/<int:emp_id>/",get_employee_details)

]
