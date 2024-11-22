from django.urls import path, include
from .views import LivroList, LivroDetail, AutorList, AutorDetail, CategoriaList, CategoriaDetail, ColecaoDetail, ColecaoList
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView




urlpatterns = [
    path('livros/', LivroList.as_view(), name='livros-list'),  
    path('livros/<int:pk>/', LivroDetail.as_view(), name='livro-detail'),
    path('autores/', AutorList.as_view(), name='autores-list'),
    path('autores/<int:pk>/', AutorDetail.as_view(), name='autor-detail'),
    path('categorias/', CategoriaList.as_view(), name='categorias-list'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),
    path('colecoes/', ColecaoList.as_view(), name='colecoes-list'),  # Listar/criar coleções
    path('colecoes/<int:pk>/', ColecaoDetail.as_view(), name='colecoes-detail'),  # Detalhes/editar/excluir

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
]
