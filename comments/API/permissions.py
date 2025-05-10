from rest_framework.permissions import BasePermission
from comments.models import Comment


# class IsOwnerOrReadAndCreateOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method == 'GET' or request.method == 'POST':
#             return True
#         else:
#             id_comment = view.kwargs['pk']
#             comment = Comment.objects.get(pk=id_comment)
#
#             id_user = request.user.pk
#             id_user_comment = comment.user_id
#
#             if id_user == id_user_comment:
#                 return True
#
#             return False

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        # Permitir GET (lista) y POST (crear)
        if request.method in ['GET', 'POST', 'PUT', 'DELETE']: # ['GET', 'POST']:
            return True
        # Para otros métodos (PUT, PATCH, DELETE), verificar autenticación
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Esta función solo se llama cuando se accede a un objeto específico (con pk)
        # Por ejemplo: GET /api/comments/1/

        # Permitir lectura (GET) siempre
        if request.method == 'GET':
            return True

        # Para edición o eliminación, verificar si el usuario es dueño del comentario
        return obj.user_id == request.user.pk