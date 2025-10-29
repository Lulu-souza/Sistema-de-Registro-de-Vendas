import time
from typing import List
from item_pedido import ItemPedido
from produto import Produto
from cliente import Cliente

class Pedido:
    proximo_id = 1

    def __init__(self, cliente: Cliente, id_pedido: int = None,data_hora: str = None, status: str = "Aberto"):
        # --- Validação do cliente ---
        if not isinstance(cliente, Cliente):
            raise TypeError("O cliente deve ser uma instância da classe Cliente.")
        
        # Permite passar ID e outros dados ao carregar (desserializar)
        if id_pedido is not None:
            self.id_pedido = id_pedido
        else:
            self.id_pedido = Pedido.proximo_id
            Pedido.proximo_id += 1
        
        self.cliente = cliente
        self.data_hora = data_hora if data_hora else time.strftime("%d/%m/%Y %H:%M:%S")
        self.itens: List[ItemPedido] = []
        self.status = "Aberto"

    def to_dict(self):
            return {
            "id_pedido": self.id_pedido,
            # Serializa o Cliente associado
            "cliente": self.cliente.to_dict(), 
            "data_hora": self.data_hora,
            "status": self.status,
            # Serializa a lista de ItemPedidos (chave para ItemPedido.to_dict())
            "itens": [item.to_dict() for item in self.itens],
            "valor_total": self.calcular_valor_total() 
        }
    
    @classmethod
    def from_dict(cls, dados: dict):
        # Cria um objeto Pedido a partir de um dicionário (JSON)
        
        # 1. Garante que o proximo_id seja mantido atualizado
        if dados['id_pedido'] >= cls.proximo_id:
            cls.proximo_id = dados['id_pedido'] + 1
            
        # 2. Recria o objeto Cliente
        cliente_recriado = Cliente.from_dict(dados['cliente']) 
        
        # 3. Cria o objeto Pedido
        pedido = cls(
            cliente=cliente_recriado,
            id_pedido=dados['id_pedido'],
            data_hora=dados['data_hora'],
            status=dados['status']
        )
        
        # 4. Recria e adiciona os itens
        for item_dict in dados['itens']:
            item_recriado = ItemPedido.from_dict(item_dict)
            pedido.itens.append(item_recriado)
            
        return pedido

    def adicionar_produto(self, produto: Produto, quantidade: float):
        # --- Validações ---
        if not isinstance(produto, Produto):
            raise TypeError("O produto deve ser uma instância da classe Produto.")
        if not isinstance(quantidade, (int, float)) or quantidade <= 0:
            raise ValueError("A quantidade deve ser um número positivo.")
        if self.status != "Aberto":
            raise ValueError("Não é possível adicionar produtos a um pedido fechado.")

        # Verifica se o produto já está no pedido
        for item in self.itens:
            if item.produto.id_produto == produto.id_produto:
                item.quantidade += quantidade 
                print(f"Produto {produto.nome} atualizado. Nova qtd: {item.quantidade} m³.")
                return

        novo_item = ItemPedido(produto, quantidade)
        self.itens.append(novo_item)
        print(f'Produto "{produto.nome}" adicionado.')

    def remover_produto(self, produto: Produto):
        if not isinstance(produto, Produto):
            raise TypeError("O produto deve ser uma instância da classe Produto.")
        if self.status != "Aberto":
            raise ValueError("Não é possível remover produtos de um pedido fechado.")

        item_a_remover = next((item for item in self.itens if item.produto.id_produto == produto.id_produto), None)
        if item_a_remover:
            self.itens.remove(item_a_remover)
            print(f"Produto '{produto.nome}' removido.")
        else:
            raise ValueError(f"O produto '{produto.nome}' não está no pedido.")

    def calcular_valor_total(self) -> float:
        return sum(item.calcular_subtotal() for item in self.itens)

    def fechar_pedido(self):
        if not self.itens:
            raise ValueError("Não é possível fechar um pedido sem itens.")
        if self.status == "Fechado":
            raise ValueError("O pedido já está fechado.")
        self.status = "Fechado"
        print(f"\nPedido {self.id_pedido} FECHADO. Total: R$ {self.calcular_valor_total():.2f}")

    def __str__(self) -> str:
        resumo = f"\n--- Pedido Nº {self.id_pedido} ({self.status}) ---\n"
        resumo += f"Data: {self.data_hora}\n"
        resumo += f"Cliente: {self.cliente.nome}\n"
        resumo += "ITENS DO PEDIDO:\n"
        for item in self.itens:
            resumo += str(item) + "\n"
        resumo += f"---------------------------------\n"
        resumo += f"VALOR FINAL: R$ {self.calcular_valor_total():.2f}\n"
        return resumo