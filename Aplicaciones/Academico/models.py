from django.db import models
from django.utils.html import format_html

from .choices import sexos

class Docente(models.Model):
    apellido_paterno = models.CharField(max_length=20, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=20, verbose_name='Apellido Materno')
    nombres = models.CharField(max_length=20, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    sexo=models.CharField(max_length=1, choices=sexos, default = 'F')

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)

    def __str__(self) -> str:
        return self.nombre_completo()
    
    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        db_table='docente'
        ordering=['apellido_paterno', '-apellido_materno'] #Apellido materno como 1er criterio en forma ascendente, 
                                                            #Apellido paterno como 2do criterio en forma descendente

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
  
    docente=models.ForeignKey(Docente, null = True, blank = True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        texto="{0}({1})"
        return texto.format(self.nombre, self.creditos)
    
    def coloreado(self):
        if self.creditos > 4:
            return format_html('<span style="color: purple;">{0}</span>'.format(self.nombre))
        else:
            return format_html('<span style="color: blue;">{0}</span>'.format(self.nombre))

    coloreado.short_description = 'NOMBRE'
    

