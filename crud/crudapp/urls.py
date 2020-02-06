from django.urls import path
from . import  views

urlpatterns = [
    path('', views.employee_form, name="employee_insert"), #get & post request for insert operation
    path('emplist/', views.employee_list, name="employee_list"),
    path('update/<int:id>', views.employee_update, name='employee_update'),# get & post request for update operation
    path('delete/<int:id>', views.employee_delete, name='employee_delete')
]
