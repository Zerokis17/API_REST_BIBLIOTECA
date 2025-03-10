from django.db import models

# django crea de manera automatica un campo id que es la llave primaria

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)

class Editorial(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True, null=True)

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    isbn = models.CharField(max_length=20, unique=True)
    anio_publicacion = models.IntegerField()
    # LLAVE FORANEA PARA DECIR QUE UN LIBRO TIENE UNICO AUTOR
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    # LLAVE FORANEA PARA DECIR QUE UN LIBRO TIENE UNICA EDITORIAL
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_membresia = models.DateField(auto_now_add=True)

class Prestamo(models.Model):
    # LLAVE FORANEA PARA DECIR QUE UN LIBRO SE PUEDE PRESTAR VARIAS VECES
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    # LLAVE FORANEA PARA DECIR QUE UN MIEMBRO PUEDE TENER VARIOS PRESTAMOS
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(blank=True, null=True)
