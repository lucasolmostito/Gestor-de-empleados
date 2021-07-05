from django.urls import path
from . import views

app_name = 'departments_app'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('departments/', views.DepartmentsListView.as_view(), name='departments-list'),
    path('employees-by-department/<id>/', views.EmployeesByDepartmentListView.as_view(), name='employees-by-department'),
    path('añadir-departamento/', views.AddDepartmentFormView.as_view(), name='add-department'),
]