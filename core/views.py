from rest_framework import generics
from .models import Livro, Autor, Categoria
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer
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
