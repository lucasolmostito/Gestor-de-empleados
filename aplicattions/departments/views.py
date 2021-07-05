from aplicattions import departments
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from .models import Departments
from aplicattions.employees.models import Employees
from .forms import AddDepartmentForm
from django.urls import reverse_lazy


class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    

class DepartmentsListView(ListView):
    template_name = 'departments/list.html'
    context_object_name = 'departments'
    model = Departments
    
class EmployeesByDepartmentListView(ListView):
    template_name = 'departments/employees_by_department.html'
    context_object_name = 'employees_department'
    paginate_by = 10
    
    def get_queryset(self):
        id = self.kwargs['id']
        queryset = Employees.objects.filter(
            department__id = id
        )   
        return queryset
    
class AddDepartmentFormView(FormView):
    template_name = 'departments/add_department.html'
    form_class = AddDepartmentForm
    success_url = reverse_lazy('departments_app:departments-list')
    
    def form_valid(self, form):
        department = form.cleaned_data['department']
        shorname = form.cleaned_data['shorname']
        dep = Departments.objects.create(    
            name = department,
            shorname = shorname
        )
        
        name = form.cleaned_data['name']
        surname = form.cleaned_data['surname']
        adress = form.cleaned_data['adress']
        email = form.cleaned_data['email']
        number = form.cleaned_data['number']
        image = form.cleaned_data['image']
        Employees.objects.create(
            name = name,
            surname = surname,
            full_name = name + ' ' + surname,
            adress = adress,
            email = email,
            number = number,
            image = image,
            job = '2',
            department = dep
        )
        return super(AddDepartmentFormView, self).form_valid(form)


