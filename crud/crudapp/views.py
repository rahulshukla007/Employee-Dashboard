from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    context = {"employee_list":Employee.objects.all()}
    return render(request, 'crudapp/employee_list.html', context)

#insert and update operatiom
def employee_form(request):
    try:
        if request.method == "GET":
            form = EmployeeForm()
            return render(request, 'crudapp/employee_form.html', {'form':form})
        else:
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/emplist')
    except Exception as e:
        print(e)

def employee_update(request,id):
    #this will take to edit page
    if request.method =="GET":
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=employee)
        return render(request, 'crudapp/employee_form.html', {'form': form})
    else:#this is for post request when we update the form
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/emplist')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/emplist')

