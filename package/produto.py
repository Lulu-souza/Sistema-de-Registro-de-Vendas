class Produto:
    
    proximo_id = 1 # para ter o ID do pruduto na frente
    
    def __init__(self, nome: str, preco_por_metro: float):
        # validação do nome
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome do produto inválido. Deve ser uma string não vazia.")
        if not all(c.isalpha() or c.isspace() for c in nome.replace(" ", "")):
            raise ValueError(f"Nome do produto inválido: '{nome}'. Deve conter apenas letras e espaços.")
        # Validação do preco_por_metro
        if not isinstance(preco_por_metro, (int, float)):
            raise TypeError("Preço por metro deve ser um número.")
        if preco_por_metro <= 0:
            raise ValueError("Preço por metro deve ser maior que zero.")
        
        self.id_produto = Produto.proximo_id 
        Produto.proximo_id += 1 
        self.nome = nome.strip()
        self.preco_por_metro = preco_por_metro

    def calcular_preco_total(self, quantidade: float):
        
        if not isinstance(quantidade, (int, float)):
            raise TypeError("A quantidade deve ser um número.")
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        
        return self.preco_por_metro * quantidade
    
    def __str__(self):
        return f"[{self.id_produto}] {self.nome} (R${self.preco_por_metro:.2f}/m³) "
    
class Areia(Produto):
    
    preco_fixo = 110 
    tipos_validos = {'Fina', 'Media', 'Grossa'} 
    def __init__(self, tipo: str):
        
        if tipo not in self.tipos_validos:
            raise ValueError(f"Tipo de areia inválido: '{tipo}'. Tipos válidos: {self.tipos_validos}")

        super().__init__(f"Areia {tipo}", self.preco_fixo) # vai acessar o preço fixo 
        self.tipo = tipo

class Barro(Produto):
    preco_fixo = 50
    cores_validas = {'Vermelho', 'Branco'}
    def __init__(self, cor:str):
        
        if cor not in self.cores_validas:
            raise ValueError(f"Cor inválida: '{cor}'. Tipos válidos: {self.cores_validas}")
        
        super().__init__(f"Barro {cor}", self.preco_fixo)
        self.cor = cor

class Brita(Produto):
    preco_fixo = 200
    tamanhos_válidos = {0, 1, 0.75}
    def __init__(self, tamanho:int):
        
        if not isinstance(tamanho, (int, float)):
            raise ValueError(f"O tamanho da brita deve ser um número (0, 1 ou 0.75(3/4))")
        
        if tamanho not in self.tamanhos_válidos:
            raise ValueError(f"Tamanho inválido: '{tamanho}'. Use 0, 1 ou 0.75 para 3/4")
        
        super().__init__(f"Brita", self.preco_fixo)
        self.tamanho = tamanho
