from aplicattions import employees
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from .models import Employees
from .forms import EmployeesForm
from django.urls import reverse_lazy

from aplicattions.employees import models

# Create your views here.

class EmployeesListView(ListView):
    template_name = 'employees/list.html'
    context_object_name = 'employees'
    paginate_by = 10
    
    def get_queryset(self):
        kword = self.request.GET.get('kword','')
        lista = Employees.objects.filter(
            full_name__icontains = kword
        )
        return lista
    
class EmployeesAdminListView(ListView):
    template_name = 'employees/admin_list.html'
    context_object_name = 'employees'
    paginate_by = 10
    
    def get_queryset(self):
        kword = self.request.GET.get('kword','')
        lista = Employees.objects.filter(
            full_name__icontains = kword
        )
        return lista
    
class EmployeesAdminUpdateView(UpdateView):
    template_name = 'employees/update.html'
    model = Employees
    fields = [
        'name',
        'surname',
        'adress',
        'number',
        'email',
        'job',
        'department',
        'image',
        'skills',
    ]
    success_url = reverse_lazy('employees_app:list-employees-admin')
    context_object_name = 'employees'
    
class EmployeesAdminDeleteView(DeleteView):
    template_name = 'employees/delete.html'
    model = Employees
    success_url = reverse_lazy('employees_app:list-employees-admin')
    context_object_name = 'employees'
    
class EmployeesCreateView(CreateView):
    template_name = 'employees/create.html'
    model = Employees
    form_class = EmployeesForm
    success_url = reverse_lazy('employees_app:list-employees')
    
    def form_valid(self, form):
        # Concatenar nombre y apellido
        empleado = form.save(commit=False)
        empleado.full_name = empleado.name + ' ' + empleado.surname
        empleado.save()
        return super(EmployeesCreateView, self).form_valid(form)
    
class EmployeeDetailView(DetailView):
    template_name = 'employees/employee_detail.html'
    model = Employees
    context_object_name = 'employee'
    
    
    
        