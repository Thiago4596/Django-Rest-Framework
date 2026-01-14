from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(
            username='admin',
            password='admin'
        )
        self.url = reverse('Estudantes-list')
    
    def test_autheticacao_de_user_com_credenciais_corretas(self):
        '''Teste para verificar a autenticação de um usuário com credenciais corretas'''
        usuario = authenticate(username='admin', password='admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def test_autheticacao_de_user_com_username_incorreto(self):
        '''Teste para verificar a autenticação de um usuário com username incorreto'''
        usuario = authenticate(username='admn', password='admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_autheticacao_de_user_com_senha_incorreta(self):
        '''Teste para verificar a autenticação de um usuário com senha incorreta'''
        usuario = authenticate(username='admin', password='admn')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_requisicao_get_autorizada(self):
        '''Teste para verificar uma requisição GET autorizada'''
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)