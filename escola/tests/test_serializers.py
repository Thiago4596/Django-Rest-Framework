from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome='Teste de modelo',
            email='teste@modelo.com',
            cpf='39625279075',
            data_nascimento='2023-02-02',
            celular='11 91234-5678'
        )
        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

    def test_verifica_campos_serializados_de_estudante(self):
        """Teste para verificar os campos serializados do Estudante"""
        dados = self.serializer_estudante.data
        self.assertEqual(set(dados.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']))

    def test_verifica_conteudos_dos_campos_serializados_de_estudante(self):
        """Teste para verificar os conteudos dos campos serializados do Estudante"""
        dados = self.serializer_estudante.data
        self.assertEqual(dados['nome'], self.estudante.nome)
        self.assertEqual(dados['email'], self.estudante.email)
        self.assertEqual(dados['cpf'], self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'], self.estudante.data_nascimento)
        self.assertEqual(dados['celular'], self.estudante.celular)

class SerializerCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            codigo='CURSO1',
            descricao='Descrição do curso 1',
            nivel='I'
        )
        self.serializer_curso = CursoSerializer(instance=self.curso)

    def test_verifica_campos_serializados_de_curso(self):
        """Teste para verificar os campos serializados do Curso"""
        dados = self.serializer_curso.data
        self.assertEqual(set(dados.keys()), set(['id', 'codigo', 'descricao', 'nivel']))

    def test_verifica_conteudos_dos_campos_serializados_de_curso(self):
        """Teste para verificar os conteudos dos campos serializados do Curso"""
        dados = self.serializer_curso.data
        self.assertEqual(dados['codigo'], self.curso.codigo)
        self.assertEqual(dados['descricao'], self.curso.descricao)
        self.assertEqual(dados['nivel'], self.curso.nivel)

class SerializerMatriculaTestCase(TestCase):
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
        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)

    def test_verifica_campos_serializados_de_matricula(self):
        """Teste para verificar os campos serializados da Matricula"""
        dados = self.serializer_matricula.data
        self.assertEqual(set(dados.keys()), set(['id', 'estudante', 'curso', 'periodo']))

    def test_verifica_conteudos_dos_campos_serializados_de_matricula(self):
        """Teste para verificar os conteudos dos campos serializados da Matricula"""
        dados = self.serializer_matricula.data
        self.assertEqual(dados['estudante'], self.matricula.estudante.id)
        self.assertEqual(dados['curso'], self.matricula.curso.id)
        self.assertEqual(dados['periodo'], self.matricula.periodo)