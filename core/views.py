from rest_framework import generics
from .models import Livro, Autor, Categoria, Colecao
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer, ColecaoSerializer
from .filters import LivroFilter, AutorFilter, CategoriaFilter

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter  # Adiciona o filtro personalizado
    search_fields = ['titulo', 'autor__nome', 'categoria__nome']  # Busca por prefixo
    ordering_fields = ['titulo', 'autor__nome', 'categoria__nome', 'publicado_em']  # Campos de ordenação
    name = "livro-list"

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    search_fields = ['nome']  # Busca por nome
    ordering_fields = ['nome']  # Ordenação por nome
    filterset_class = AutorFilter
    name = "autor-list"

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()  # Corrigido para Autor
    serializer_class = AutorSerializer
    name = "autor-detail"

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ['nome']  # Busca por nome
    ordering_fields = ['nome']  # Ordenação por nome
    filterset_class = CategoriaFilter  # Filtro personalizado
    name = "categoria-list"

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()  # Corrigido para Categoria
    serializer_class = CategoriaSerializer
    name = "categoria-detail"


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Colecao
from .serializers import ColecaoSerializer
from .custom_permissions import IsColecionador

class ColecaoList(generics.ListCreateAPIView):
    """
    Listar todas as coleções e permitir a criação para o usuário autenticado.

    - Qualquer usuário autenticado pode listar todas as coleções.
    - Apenas o usuário autenticado pode criar uma nova coleção.
    """
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Vincula a nova coleção ao usuário autenticado
        serializer.save(colecionador=self.request.user)


class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Visualizar, atualizar ou excluir uma coleção.

    - Qualquer usuário autenticado pode visualizar qualquer coleção.
    - Apenas o colecionador pode editar ou excluir a coleção.
    """
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsAuthenticated, IsColecionador]