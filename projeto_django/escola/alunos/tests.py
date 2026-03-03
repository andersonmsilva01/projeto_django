from django.test import TestCase
from .models import Aluno

class AlunoModelTest(TestCase):

    def test_criar_aluno(self):
        aluno = Aluno.objects.create(
            nome="Teste",
            idade=20,
            email="teste@email.com"
        )
        self.assertEqual(aluno.nome, "Teste")
        self.assertTrue(aluno.matriculado)

class AlunoViewTest(TestCase):

    def test_lista_alunos_status(self):
        response = self.client.get('/alunos/')
        self.assertEqual(response.status_code, 200)

def test_idade_aluno(self):
    aluno = Aluno.objects.create(
        nome="Carlos",
        idade=25,
        email="carlos@email.com"
    )
    self.assertEqual(aluno.idade, 25)

def test_rota_novo_aluno(self):
    response = self.client.get('/alunos/novo/')
    self.assertEqual(response.status_code, 302)