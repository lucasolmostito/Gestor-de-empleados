from django.db import models

class Departments(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shorname = models.CharField('Nombre Corto', max_length=50)
    anulate = models.BooleanField('Anulado', default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
