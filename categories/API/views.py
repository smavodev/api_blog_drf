from rest_framework.viewsets import ModelViewSet

from categories.models import Category
from categories.API.serializers import CategorySerializer
from categories.API.permissions import IsAdminOrReadOnly


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'  # cambia el ID * Slug para Obtener, Editar o eliminar una categoría


