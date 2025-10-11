import unittest
from cliente import Cliente

class TestCliente(unittest.TestCase):

# teste cliente: 

    def test_cliente_valido(self):
        c = Cliente("Maria Silva", "11987654321", "Rua das Flores, 100")
        self.assertEqual(c.nome, "Maria Silva")
        self.assertEqual(c.telefone, "11987654321")
        self.assertEqual(c.endereco, "Rua das Flores, 100")

# teste nome: 

    def test_nome_vazio(self):
        with self.assertRaises(ValueError):
            Cliente("", "11987654321", "Rua A")

    def test_nome_com_numero(self):
        with self.assertRaises(ValueError):
            Cliente("Maria123", "11987654321", "Rua A")

# teste telefone: 

    def test_telefone_com_letra(self):
        with self.assertRaises(ValueError):
            Cliente("Ana", "11A7654321", "Rua A")

    def test_telefone_tipo_invalido(self):
        with self.assertRaises(ValueError):
            Cliente("Ana", 11987654321, "Rua A")

# teste endereço: 

    def test_endereco_vazio(self):
        with self.assertRaises(ValueError):
            Cliente("Pedro", "11987654321", "")


if __name__ == "__main__":
    unittest.main()