from django.test import TestCase
from blog.models import Associado

# Captura a resposta e verifica se a url está funcionando
class Test_URL(TestCase):
    def test_page(self):
      response = self.client.get('/')
      self.assertEquals(response.status_code, 200) #página respondeu sem erros


# Verifica se os dados inseridos forma gravados
class Test_model(TestCase):
    def test_save (self):
        associado=Associado()
        associado.numero_associado = '123'
        associado.nome = 'Pessoa'
        associado.telefone='(11)3456-7890'
        associado.celular='(11)12345-6789'
        associado.email= 'pessoa@email.com'
        associado.save()
        record = Associado.objects.get(pk=1)
        self.assertEqual(record, associado)


