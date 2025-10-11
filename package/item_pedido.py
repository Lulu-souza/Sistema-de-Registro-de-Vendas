from produto import Produto
class ItemPedido:

    def __init__(self, produto: Produto, quantidade: float):
        # --- Validação do produto ---
        if not isinstance(produto, Produto):
            raise TypeError("O produto deve ser uma instância da classe Produto.")
        
        # --- Validação da quantidade ---
        if not isinstance(quantidade, (int, float)):
            raise TypeError("A quantidade deve ser um número.")
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        
        self.produto = produto
        self.quantidade = quantidade


    def calcular_subtotal(self):

        return self.produto.calcular_preco_total(self.quantidade)
    
    def __str__(self):
        return (f"  > {self.quantidade} m³ de {self.produto.nome} "
                f"(Subtotal: R$ {self.calcular_subtotal():.2f})")