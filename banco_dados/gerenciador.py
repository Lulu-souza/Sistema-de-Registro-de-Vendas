import json
from package.cliente import Cliente
from package.pedido import Pedido
from package.produto import Produto
from package.item_pedido import ItemPedido



# Nome e caminho do arquivo de banco de dados
ARQUIVO_BANCO = 'banco_dados/banco.json' 

def carregar_dados():
    
    #Tenta carregar os dados de clientes, pedidos e produtos do banco.json.
    #Retorna uma estrutura vazia se o arquivo não existir ou for inválido.
    
    try:
        with open(ARQUIVO_BANCO, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            # Garantir que as chaves essenciais existam
            if 'clientes' not in dados: dados['clientes'] = []
            if 'pedidos_fechados' not in dados: dados['pedidos_fechados'] = []
            # Produtos pré-cadastrados não precisam ser carregados, mas a chave pode ser útil
            if 'produtos' not in dados: dados['produtos'] = [] 
            return dados
    except FileNotFoundError:
        print(f"Arquivo {ARQUIVO_BANCO} não encontrado. Iniciando com dados vazios.")
        return {
            "clientes": [], 
            "pedidos_fechados": [],
            "produtos": [] 
        }
    except json.JSONDecodeError:
        print(f"Erro ao ler o arquivo {ARQUIVO_BANCO}. Iniciando com dados vazios.")
        return {
            "clientes": [], 
            "pedidos_fechados": [],
            "produtos": [] 
        }

def salvar_dados(dados):
    # Salva a estrutura de dados (clientes, pedidos) no banco.json.
    try:
        with open(ARQUIVO_BANCO, 'w', encoding='utf-8') as f:
            # Usar 'indent=4' para facilitar a leitura humana do JSON
            json.dump(dados, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar dados no arquivo {ARQUIVO_BANCO}: {e}")