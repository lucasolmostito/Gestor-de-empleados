from django.db import models
from django.db.models.fields import EmailField
from aplicattions.departments.models import Departments

class Skills(models.Model):
    skill = models.CharField('Habilidad', max_length=50)
    
    def __str__(self):
        return self.skill
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        

class Employees(models.Model):
    JOB_CHOICES = (
        ('0', 'Gerente'),
        ('1', 'Recepción'),
        ('2', 'Gestión'),
        ('3', 'Servicios'),
        ('4', 'Comercial'),
        ('5', 'Recursos Humanos'),
        
    )
    name = models.CharField('Nombres', max_length=50)
    surname = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField('Nombre completo', max_length=100, blank=True)
    adress = models.CharField('Dirección', max_length=50)
    number = models.CharField('Número de teléfono', max_length=12)
    email = models.EmailField('Correo electrónico', max_length=50)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    image = models.ImageField('Imagen', upload_to='employees', blank=True, null=True)
    skills = models.ManyToManyField(Skills)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    
    
    def __str__(self):
        return self.name + ' ' + self.surname
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['surname', 'name']
        
    
    

