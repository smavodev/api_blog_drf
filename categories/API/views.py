from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from categories.API.serializers import CategorySerializer
from categories.API.permissions import IsAdminOrReadOnly


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    queryset = Category.objects.filter(published=True)
    # lookup_field = 'slug'  # cambia el ID * Slug para Obtener, Editar o eliminar una categoría
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published', 'title']

