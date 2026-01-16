from django.test import TestCase
from escola.models import Estudante,Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixtures(self):
        """"Teste que verifica o carregamento da fixtures"""
        estudante = Estudante.objects.get(cpf='93774077886')
        curso = Curso.objects.get(pk=4)
        self.assertEqual(estudante.celular, "13 99715-5087")
        self.assertEqual(curso.codigo, "CPOO1")