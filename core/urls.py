from django.urls import path
from .views import livro_list_create, livro_detail

urlpatterns = [
    path('livros/', livro_list_create, name='livros-list-create'),
    path('livros/<int:pk>/', livro_detail, name='livro-detail'),
]
