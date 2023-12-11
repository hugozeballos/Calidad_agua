from django.db import models

# Create your models here.
class Indicadores(models.Model):
    conductividad=models.DecimalField(max_digits=5, decimal_places=2)
    orp=models.DecimalField(max_digits=5, decimal_places=2)
    oxigeno_disuelto=models.DecimalField(max_digits=5, decimal_places=2)
    ph=models.DecimalField(max_digits=5, decimal_places=2)
    porcentaje_oxigeno=models.DecimalField(max_digits=5, decimal_places=2)
    profundidad=models.DecimalField(max_digits=5, decimal_places=2)
    salinidad=models.DecimalField(max_digits=5, decimal_places=2)
    solidos_suspendidos_totales=models.DecimalField(max_digits=5, decimal_places=2)
    temperatura=models.DecimalField(max_digits=5, decimal_places=2)
    transparencia=models.DecimalField(max_digits=5, decimal_places=2)
    conductividad_unidad_medida = models.CharField(max_length=10)
    muestra_id = models.CharField(max_length=10)
    orp_unidad_medida = models.CharField(max_length=10)
    oxigeno_disuelto_unidad_medida = models.CharField(max_length=10)
    ph_unidad_medida = models.CharField(max_length=10)
    porcentaje_oxigeno_unidad_medida = models.CharField(max_length=10)
    profundidad_unidad_medida = models.CharField(max_length=10)
    salinidad_unidad_medida = models.CharField(max_length=10)
    solidos_suspendidos_totales_unidad_medida = models.CharField(max_length=10)
    temperatura_unidad_medida = models.CharField(max_length=10)
    transparencia_unidad_medida = models.CharField(max_length=10)
    id_indicadores = models.CharField(max_length=10)

class proyectos(models.Model):
    latitud=models.DecimalField(max_digits=11, decimal_places=9)
    longitud=models.DecimalField(max_digits=11, decimal_places=9)
    fecha=models.DateField()
    descripcion = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    localidades = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=50)
    tipo_recurso = models.CharField(max_length=50)
    usuario_id = models.CharField(max_length=50)
    zona = models.CharField(max_length=50)
    id_proyectos = models.CharField(max_length=50)

class usuarios(models.Model):
    fecha_registro=models.DateField()
    apellido = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    passsword = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    id_usuarios = models.CharField(max_length=50)

class usuarios_proyectos(models.Model):
    proyectos_id = models.CharField(max_length=50)
    usuario_id = models.CharField(max_length=50)

class proyectos_muestra(models.Model):
    muestra_id = models.CharField(max_length=50)
    proyecto_id = models.CharField(max_length=50)

class muestras(models.Model):
    latitud=models.DecimalField(max_digits=10, decimal_places=9)
    longitud=models.DecimalField(max_digits=10, decimal_places=9)
    fecha=models.DateField()
    numero=models.IntegerField()
    indicador_id = models.CharField(max_length=50)
    laboratorio = models.CharField(max_length=50)
    proyecto_id = models.CharField(max_length=50)
    calidad = models.CharField(max_length=50)
    id_muestras = models.CharField(max_length=50)

