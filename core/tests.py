from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Colecao

class ColecaoTests(APITestCase):
    def setUp(self):
        # Criação do usuário
        self.user = User.objects.create_user(username="testuser", password="password")

        # Criação do token de autenticação
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Criação de uma coleção associada ao usuário
        self.colecao = Colecao.objects.create(nome="Minha Coleção", colecionador=self.user)

    def test_criar_colecao(self):
        data = {'nome': 'Nova Coleção', 'descricao': 'Descrição da coleção'}
        response = self.client.post('/colecoes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], 'Nova Coleção')

    def test_editar_colecao(self):
        data = {'nome': 'Coleção Atualizada'}
        response = self.client.put(f'/colecoes/{self.colecao.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Coleção Atualizada')

    def test_deletar_colecao(self):
        response = self.client.delete(f'/colecoes/{self.colecao.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
