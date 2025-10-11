import unittest
from produto import Produto
from item_pedido import ItemPedido

class TestItemPedido(unittest.TestCase):

    def setUp(self):
        self.produto = Produto("Areia Fina", 100.0)

    # ---------- TESTES DE CRIAÇÃO ----------
    def test_item_pedido_valido(self):
        item = ItemPedido(self.produto, 2)
        self.assertEqual(item.produto, self.produto)
        self.assertEqual(item.quantidade, 2)

    def test_produto_invalido(self):
        with self.assertRaises(TypeError):
            ItemPedido("Produto errado", 2)

    def test_quantidade_negativa(self):
        with self.assertRaises(ValueError):
            ItemPedido(self.produto, -1)

    def test_quantidade_zero(self):
        with self.assertRaises(ValueError):
            ItemPedido(self.produto, 0)

    def test_quantidade_tipo_invalido(self):
        with self.assertRaises(TypeError):
            ItemPedido(self.produto, "duas")

    # ---------- TESTES DE CÁLCULO ----------
    def test_calcular_subtotal(self):
        item = ItemPedido(self.produto, 3)
        self.assertEqual(item.calcular_subtotal(), 300.0)

    # ---------- TESTE DE FORMATAÇÃO ----------
    def test_str_format(self):
        item = ItemPedido(self.produto, 1.5)
        esperado = "  > 1.5 m³ de Areia Fina (Subtotal: R$ 150.00)"
        self.assertEqual(str(item), esperado)


if __name__ == "__main__":
    unittest.main()