from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_se_eh_possivel_lancar_uma_movimentacao_financeira(self):


        # William precisando de um sistema de controle financeiro para ajudar no 
        # controle financeiro da sua casa. Ele decidiu fazer um sistema web para ele

        self.browser.get('http://localhost:8000')

        # Ele percebe que o título da pagina e o cabeçalho mencionam contas a pagar e receber

        self.assertIn('Contas: a pagar e receber', self.browser.title)
        self.fail('Fim dos teste')

        # Ele é convidado a inserir em um campo um valor e uma descrição de uma movimentação financeira e a data
        # ele ainda pode marcar se já foi concretizada ou não

        # Ele digita "-32,90" "Netflix" "12/05/2020" e marca como concluído.

        # Quando ele aperta Enter a pagina é atualizada, e agora lista
        # "1: -32,90 - Netflix 12 de maio de 2020 pago"

if __name__ == "__main__":
    unittest.main(warnings='ignore')