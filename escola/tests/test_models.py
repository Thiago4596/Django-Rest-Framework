from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEsudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome='Teste de modelo',
            email='teste@modelo.com',
            cpf='39625279075',
            data_nascimento='2023-02-02',
            celular='11 91234-5678'
        )
    
    def test_verifica_atributos_de_estudante(self):
        """Teste para verificar os atributos do modelo Estudante"""
        self.assertEqual(self.estudante.nome, 'Teste de modelo')
        self.assertEqual(self.estudante.email, 'teste@modelo.com')
        self.assertEqual(self.estudante.cpf, '39625279075')
        self.assertEqual(self.estudante.data_nascimento, '2023-02-02')
        self.assertEqual(self.estudante.celular, '11 91234-5678')

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo='CURSO1',
            descricao='Descrição do curso 1',
            nivel='I'
        )
    
    def test_verifica_atributos_de_curso(self):
        """Teste para verificar os atributos do modelo Curso"""
        self.assertEqual(self.curso.codigo, 'CURSO1')
        self.assertEqual(self.curso.descricao, 'Descrição do curso 1')
        self.assertEqual(self.curso.nivel, 'I')

class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome='Aluno Matricula',
            email='aluno@matricula.com',
            cpf='12345678901',
            data_nascimento='2000-01-01',
            celular='11 91234-5678'
        )
        self.curso = Curso.objects.create(
            codigo='CURSO2',
            descricao='Descrição do curso 2',
            nivel='A'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso
        )
   
    def test_verifica_atributos_de_matricula(self):
        """Teste para verificar os atributos do modelo Matricula"""
        self.assertEqual(self.matricula.estudante.nome, 'Aluno Matricula')
        self.assertEqual(self.matricula.curso.codigo, 'CURSO2')