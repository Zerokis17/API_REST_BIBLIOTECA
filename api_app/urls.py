from django.urls import path, include
from rest_framework import routers
from api_app.views import AutorViewSet, EditorialViewSet, LibroViewSet, MiembroViewSet, PrestamoViewSet

router = routers.DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'editoriales', EditorialViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'miembros', MiembroViewSet)
router.register(r'prestamos', PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
