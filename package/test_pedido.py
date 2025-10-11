import unittest
from pedido import Pedido
from cliente import Cliente
from produto import Produto
from item_pedido import ItemPedido

class TestPedido(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("Maria", "11987654321", "Rua das Flores")
        self.produto1 = Produto("Areia Fina", 100)
        self.produto2 = Produto("Barro Vermelho", 50)
        self.pedido = Pedido(self.cliente)

    # ---------- TESTES DE CRIAÇÃO ----------
    def test_pedido_valido(self):
        self.assertEqual(self.pedido.status, "Aberto")
        self.assertEqual(self.pedido.cliente.nome, "Maria")
        self.assertIsInstance(self.pedido.itens, list)

    def test_cliente_invalido(self):
        with self.assertRaises(TypeError):
            Pedido("Cliente errado")

    # ---------- TESTES ADICIONAR PRODUTO ----------
    def test_adicionar_produto_valido(self):
        self.pedido.adicionar_produto(self.produto1, 2)
        self.assertEqual(len(self.pedido.itens), 1)
        self.assertEqual(self.pedido.itens[0].quantidade, 2)

    def test_adicionar_quantidade_invalida(self):
        with self.assertRaises(ValueError):
            self.pedido.adicionar_produto(self.produto1, -1)
        with self.assertRaises(ValueError):
            self.pedido.adicionar_produto(self.produto1, 0)

    def test_adicionar_produto_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.pedido.adicionar_produto("produto", 2)

    def test_adicionar_produto_em_pedido_fechado(self):
        self.pedido.fechar_pedido = lambda: setattr(self.pedido, "status", "Fechado")
        self.pedido.status = "Fechado"
        with self.assertRaises(ValueError):
            self.pedido.adicionar_produto(self.produto1, 1)

    # ---------- TESTES REMOVER PRODUTO ----------
    def test_remover_produto_existente(self):
        self.pedido.adicionar_produto(self.produto1, 1)
        self.pedido.remover_produto(self.produto1)
        self.assertEqual(len(self.pedido.itens), 0)

    def test_remover_produto_inexistente(self):
        with self.assertRaises(ValueError):
            self.pedido.remover_produto(self.produto1)

    def test_remover_produto_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.pedido.remover_produto("produto")

    def test_remover_produto_pedido_fechado(self):
        self.pedido.adicionar_produto(self.produto1, 1)
        self.pedido.status = "Fechado"
        with self.assertRaises(ValueError):
            self.pedido.remover_produto(self.produto1)

    # ---------- TESTES CALCULAR TOTAL ----------
    def test_calcular_valor_total(self):
        self.pedido.adicionar_produto(self.produto1, 2)
        self.pedido.adicionar_produto(self.produto2, 1)
        total = self.pedido.calcular_valor_total()
        self.assertEqual(total, 100*2 + 50*1)

    # ---------- TESTES FECHAR PEDIDO ----------
    def test_fechar_pedido_sem_itens(self):
        with self.assertRaises(ValueError):
            self.pedido.fechar_pedido()

    def test_fechar_pedido_valido(self):
        self.pedido.adicionar_produto(self.produto1, 1)
        self.pedido.fechar_pedido()
        self.assertEqual(self.pedido.status, "Fechado")

    def test_fechar_pedido_ja_fechado(self):
        self.pedido.adicionar_produto(self.produto1, 1)
        self.pedido.fechar_pedido()
        with self.assertRaises(ValueError):
            self.pedido.fechar_pedido()


if __name__ == "__main__":
    unittest.main()