import re
class Cliente:
    def __init__(self, nome: str, telefone: str, endereco: str):
        # Validação do Nome (aceita espaços)
        if not isinstance(nome, str) or not nome.replace(" ", "").isalpha():
            raise ValueError(f"Nome inválido: '{nome}'. O nome deve conter apenas letras e espaços.")

        # Validação do Telefone (aceita apenas números e símbolos)
        padrao_telefone = r'^[\d\s\-\+\(\)]+$'
        if not isinstance(telefone, str) or not re.match(padrao_telefone, telefone.strip()):
            raise ValueError(f"Telefone inválido: '{telefone}'. Use apenas números e símbolos como () - +.")
        
        #Validação do endereço:
        if not endereco or not endereco.strip():
            raise ValueError("Endereço inválido. O campo não pode estar vazio.")
        
        # Atribuição se a validação passar
        self.nome = nome.strip()
        self.telefone = telefone.strip()
        self.endereco = endereco.strip() # Endereço geralmente aceita qualquer string, então a validação é mínima
        
    def to_dict(self):
        return {
            
            "nome": self.nome,
            "telefone": self.telefone,
            "endereco": self.endereco
        }
        
    @classmethod
    def from_dict(cls, dados: dict):
        # Cria um objeto Cliente a partir de um dicionário (JSON).
        
        return cls(
            nome=dados['nome'],
            telefone=dados['telefone'],
            endereco=dados['endereco'],
        )
    

    def __str__(self):
        return f"Cliente: {self.nome}\n Telefone: {self.telefone}\n Endereço: {self.endereco}"