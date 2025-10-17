from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Tarea
from .serializers import TareaSerializer

class TareaPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'

class TareaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las tareas.
    Métodos disponibles: 
    - GET: Listar todas las tareas o una tarea específica.
    - POST: Crear una nueva tarea.
    - PATCH: Actualizar parcialmente una tarea existente.
    - DELETE: Eliminar una tarea.
    """
    queryset = Tarea.objects.all().order_by('-created_at')
    serializer_class = TareaSerializer
    pagination_class = TareaPagination
    http_method_names = ['get', 'post', 'patch', 'delete']
