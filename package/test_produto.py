# Testando a classe produto e suas subclasses : 
import unittest
from produto import Produto, Areia, Barro, Brita

# Testando a classe Produto: 

class TestProduto(unittest.TestCase):

    def test_valido(self):
        p = Produto('Aterro', 60)
        self.assertEqual(p.nome, "Aterro")
        self.assertEqual(p.preco_por_metro, 60) 

    def test_nome_vazio(self):
        with self.assertRaises(ValueError):
            Produto("", 100)

    def test_nome_com_numero(self):
        with self.assertRaises(ValueError):
            Produto("Areia123", 100)

    def test_preco_negativo(self):
        with self.assertRaises(ValueError):
            Produto("Areia", -10)

    def test_preco_zero(self):
        with self.assertRaises(ValueError):
            Produto("Areia", 0)

    def test_preco_invalido_tipo(self):
        with self.assertRaises(TypeError):
            Produto("Areia", "cem")

    def test_calculo_preco_total_valido(self):
        p = Produto("Aterro",60)
        self.assertEqual(p.calcular_preco_total(2), 120)

    def test_calculo_preco_total_invalido(self):
        p = Produto("Aterro", 60)
        with self.assertRaises(ValueError):
            p.calcular_preco_total(0)
        with self.assertRaises(ValueError):
            p.calcular_preco_total(-3)
        with self.assertRaises(TypeError):
            p.calcular_preco_total("duas")

# Teste da areia: 

    def test_areia_valida(self):
        a = Areia("Fina")
        self.assertIn("Fina", a.nome)

    def test_areia_invalida(self):
        with self.assertRaises(ValueError):
            Areia("Seca")

# Teste da barro:

    def test_barro_valido(self):
        b = Barro("Vermelho")
        self.assertIn("Vermelho", b.nome)

    def test_barro_invalido(self):
        with self.assertRaises(ValueError):
            Barro("Azul")

# Teste da brita :

    def test_brita_valores_validos(self):
        b1 = Brita(0)
        b2 = Brita(1)
        b3 = Brita(0.75)
        self.assertEqual(b1.tamanho, 0)
        self.assertEqual(b2.tamanho, 1)
        self.assertEqual(b3.tamanho, 0.75)

    def test_brita_valores_invalidos(self):
        with self.assertRaises(ValueError):
            Brita(2)
        with self.assertRaises(ValueError):
            Brita(-1)
        with self.assertRaises(ValueError):
            Brita("3/4")
        with self.assertRaises(ValueError):
            Brita(None)

if __name__ == "__main__":
    unittest.main()