
from rest_framework.permissions import BasePermission

class IsColecionador(BasePermission):
    """
    Permissão personalizada que permite que apenas o colecionador gerencie a coleção.
    """
    def has_object_permission(self, request, view, obj):
        # Permite leitura para todos
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Apenas o colecionador pode editar ou excluir
        return obj.colecionador == request.user