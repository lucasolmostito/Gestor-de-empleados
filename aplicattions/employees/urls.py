from django.urls import path
from . import views

app_name = 'employees_app'

urlpatterns = [
    path('lista-empleados/', views.EmployeesListView.as_view(), name='list-employees'),
    path('lista-empleados-admin/', views.EmployeesAdminListView.as_view(), name='list-employees-admin'),
    path('actualizar-empleado/<pk>/', views.EmployeesAdminUpdateView.as_view(), name='update-employee'),
    path('eliminar-empleado/<pk>/', views.EmployeesAdminDeleteView.as_view(), name='delete-employee'),
    path('crear-empleado/', views.EmployeesCreateView.as_view(), name='create-employee'),
    path('detalle-empleado/<pk>', views.EmployeeDetailView.as_view(), name='detail-employee'),
]