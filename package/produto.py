class Produto:
    
    proximo_id = 1 # para ter o ID do pruduto na frente
    
    def __init__(self, nome: str, preco_por_metro: float):
        # validação do nome
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome do produto inválido. Deve ser uma string não vazia.")
        
        # Validação do preco_por_metro
        if not isinstance(preco_por_metro, (int, float)):
            raise TypeError("Preço por metro deve ser um número.")
        if preco_por_metro <= 0:
            raise ValueError("Preço por metro deve ser maior que zero.")
        
        self.id_produto = Produto.proximo_id 
        Produto.proximo_id += 1 
        self.nome = nome.strip()
        self.preco_por_metro = preco_por_metro

    def to_dict(self):
            #Converter o objeto para um dicionario para ser usado no JSON
            return {
            "id_produto": self.id_produto,
            "nome": self.nome,
            "preco_por_metro": self.preco_por_metro,
            # Chave adicionada para identificar o tipo real do produto
            "tipo_classe": self.__class__.__name__
        }

    @classmethod
    def from_dict(cls, dados: dict):
        # Cria a subclasse correta de Produto a partir de um dicionário (JSON)
        
        # Garante que o proximo_id seja mantido atualizado
        if dados['id_produto'] >= cls.proximo_id:
            cls.proximo_id = dados['id_produto'] + 1
            
        # 1. Identifica a classe correta
        tipo_classe = dados.get("tipo_classe")
        
        if tipo_classe == "Areia":
            return Areia.from_dict(dados)
        elif tipo_classe == "Barro":
            return Barro.from_dict(dados)
        elif tipo_classe == "Brita":
            return Brita.from_dict(dados)
        else:
            # Se for um Produto genérico (não subclasse) ou tipo desconhecido
            return cls(
                nome=dados['nome'],
                preco_por_metro=dados['preco_por_metro'],
                id_produto=dados['id_produto']
            )
        
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


    def to_dict(self):
        dados = super().to_dict() # Pega os dados da classe Produto
        dados["tipo"] = self.tipo
        return dados
    
    @classmethod
    def from_dict(cls, dados: dict):
        # A subclasse Brita precisa apenas do atributo específico 'tamanho' para ser recriada
        produto = cls(tipo=dados['tipo'])
        produto.id_produto = dados['id_produto'] # Redefine o ID com o valor do JSON
        return produto

class Barro(Produto):
    preco_fixo = 50
    cores_validas = {'Vermelho', 'Branco'}
    def __init__(self, cor:str):
        
        if cor not in self.cores_validas:
            raise ValueError(f"Cor inválida: '{cor}'. Tipos válidos: {self.cores_validas}")
        
        super().__init__(f"Barro {cor}", self.preco_fixo)
        self.cor = cor

    def to_dict(self):
        dados = super().to_dict()
        dados["cor"] = self.cor
        return dados
    
    @classmethod
    def from_dict(cls, dados: dict):
        produto = cls(cor=dados['cor'])
        produto.id_produto = dados['id_produto']
        return produto

class Brita(Produto):
    preco_fixo = 200
    tamanhos_válidos = {0, 1, 0.75}
    def __init__(self, tamanho:int):
        
        if not isinstance(tamanho, (int, float)):
            raise ValueError(f"O tamanho da brita deve ser um número (0, 1 ou 0.75(3/4))")
        
        if tamanho not in self.tamanhos_válidos:
            raise ValueError(f"Tamanho inválido: '{tamanho}'. Use 0, 1 ou 0.75 para 3/4")
        
        nome = f"Brita {tamanho}" 
        super().__init__(nome, self.preco_fixo)
        self.tamanho = tamanho

    def to_dict(self):
        dados = super().to_dict()
        dados["tamanho"] = self.tamanho
        return dados
    
    @classmethod
    def from_dict(cls, dados: dict):
        produto = cls(tamanho=dados['tamanho'])
        produto.id_produto = dados['id_produto']
        return produto
