from rest_framework import viewsets
from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializer import AutorSerializer, EditorialSerializer, LibroSerializer, MiembroSerializer, PrestamoSerializer
from rest_framework import filters

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['autor__nombre', 'editorial__nombre']  # Buscar por autor o editorial



class MiembroViewSet(viewsets.ModelViewSet):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['fecha_prestamo', 'miembro__nombre']  # Buscar por fecha o miembro
