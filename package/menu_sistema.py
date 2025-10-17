from cliente import Cliente
from produto import Produto, Areia, Barro, Brita
from pedido import Pedido
from item_pedido import ItemPedido
import os
import sys

class MenuSistema:
    def __init__(self):
        
        self.Cliente = Cliente
        self.Produto = Produto
        self.Areia = Areia
        self.Barro = Barro
        self.Brita = Brita
        self.Pedido = Pedido
        self.ItemPedido = ItemPedido
        
        self.clientes_cadastrados = []
        self.pedidos_abertos = []
        self.pedidos_fechados = []
        
        # Produtos pré-cadastrados conforme suas classes
        self.produtos_disponiveis = [
            Areia("Fina"),
            Areia("Media"), 
            Areia("Grossa"),
            Barro("Vermelho"),
            Barro("Branco"),
            Brita(0),
            Brita(1),
            Brita(0.75)
        ]

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def aguardar_enter(self):
        input("\nPressione Enter para continuar...")

    def exibir_cabecalho(self, titulo):
        self.limpar_tela()
        print("=" * 60)
        print(f"{titulo:^60}")
        print("=" * 60)
        print()
    
    def menu_principal(self):
        while True:
            self.exibir_cabecalho("SISTEMA DE VENDAS - REGISTROS")
            print("1. Cadastrar Cliente")
            print("2. Criar Novo Pedido")
            print("3. Gerenciar Pedido Aberto")
            print("4. Fechar Pedido")
            print("5. Listar Pedidos Fechados")
            print("6. Listar Clientes Cadastrados")
            print("7. Listar Produtos Disponíveis")
            print("0. Sair do Sistema")
            print()
            
            opcao = input("Digite a opção desejada: ")
            
            if opcao == "1":
                self.cadastrar_cliente()
            elif opcao == "2":
                self.criar_novo_pedido()
            elif opcao == "3":
                self.gerenciar_pedido_aberto()
            elif opcao == "4":
                self.fechar_pedido()
            elif opcao == "5":
                self.listar_pedidos_fechados()
            elif opcao == "6":
                self.listar_clientes_cadastrados()
            elif opcao == "7":
                self.listar_produtos_disponiveis()
            elif opcao == "0":
                self.sair_sistema()
            else:
                print("Opção inválida! Tente novamente.")
                self.aguardar_enter()

    def cadastrar_cliente(self):
        self.exibir_cabecalho("CADASTRAR CLIENTE")
        
        try:
            print("Preencha os dados do cliente:")
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            
            cliente = self.Cliente(nome, telefone, endereco)
            self.clientes_cadastrados.append(cliente)
            print(f"\n✓ Cliente {nome} cadastrado com sucesso!")
            
        except ValueError as e:
            print(f"\n✗ Erro ao cadastrar cliente: {e}")
        except Exception as e:
            print(f"\n✗ Erro inesperado: {e}")
            
        self.aguardar_enter()

    def listar_clientes_cadastrados(self):
        self.exibir_cabecalho("CLIENTES CADASTRADOS")
        
        if not self.clientes_cadastrados:
            print("Nenhum cliente cadastrado.")
        else:
            for i, cliente in enumerate(self.clientes_cadastrados, 1):
                print(f"{i}. {cliente.nome} | {cliente.telefone} | {cliente.endereco}")
        
        self.aguardar_enter()

    def listar_produtos_disponiveis(self):
        self.exibir_cabecalho("PRODUTOS DISPONÍVEIS")
        
        print("CÓDIGO | DESCRIÇÃO | PREÇO POR m³")
        print("-" * 50)
        for produto in self.produtos_disponiveis:
            print(f"{produto.id_produto:6} | {produto.nome:15} | R$ {produto.preco_por_metro:.2f}/m³")
        print("-" * 50)
        
        self.aguardar_enter()

    def selecionar_cliente(self):
        if not self.clientes_cadastrados:
            print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
            return None
        
        print("\nClientes disponíveis:")
        for i, cliente in enumerate(self.clientes_cadastrados, 1):
            print(f"{i}. {cliente.nome} - {cliente.telefone}")
        
        try:
            opcao = int(input("\nSelecione o cliente (número): "))
            if 1 <= opcao <= len(self.clientes_cadastrados):
                return self.clientes_cadastrados[opcao - 1]
            else:
                print("Opção inválida!")
                return None
        except ValueError:
            print("Digite um número válido!")
            return None

    def criar_novo_pedido(self):
        self.exibir_cabecalho("CRIAR NOVO PEDIDO")
        
        if not self.clientes_cadastrados:
            print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
            self.aguardar_enter()
            return
        
        cliente = self.selecionar_cliente()
        if not cliente:
            self.aguardar_enter()
            return
        
        try:
            pedido = self.Pedido(cliente)
            self.pedidos_abertos.append(pedido)
            print(f"\n✓ Pedido #{pedido.id_pedido} criado para {cliente.nome}!")
            
            # Perguntar se deseja adicionar produtos agora
            print("\nDeseja adicionar produtos a este pedido agora?")
            print("1. Sim")
            print("2. Não (pode adicionar depois)")
            
            opcao = input("Opção: ")
            if opcao == "1":
                self.adicionar_produtos_pedido(pedido)
                
        except Exception as e:
            print(f"\n✗ Erro ao criar pedido: {e}")
            
        self.aguardar_enter()

    def adicionar_produtos_pedido(self, pedido):
        while True:
            self.exibir_cabecalho(f"ADICIONAR PRODUTOS - PEDIDO #{pedido.id_pedido}")
            print(f"Cliente: {pedido.cliente.nome}")
            print("\nProdutos disponíveis:")
            print("-" * 50)
            for produto in self.produtos_disponiveis:
                print(f"{produto.id_produto}. {produto.nome} - R$ {produto.preco_por_metro:.2f}/m³")
            print("-" * 50)
            
            try:
                codigo_produto = int(input("\nDigite o código do produto (0 para voltar): "))
                if codigo_produto == 0:
                    break
                
                produto_selecionado = None
                for produto in self.produtos_disponiveis:
                    if produto.id_produto == codigo_produto:
                        produto_selecionado = produto
                        break
                
                if not produto_selecionado:
                    print("Código de produto inválido!")
                    self.aguardar_enter()
                    continue
                
                quantidade = float(input(f"Quantidade de {produto_selecionado.nome} (m³): "))
                
                pedido.adicionar_produto(produto_selecionado, quantidade)
                
                print("\nDeseja adicionar outro produto?")
                print("1. Sim")
                print("2. Não")
                continuar = input("Opção: ")
                if continuar != "1":
                    break
                    
            except ValueError as e:
                print(f"Erro: {e}")
                self.aguardar_enter()
            except Exception as e:
                print(f"Erro inesperado: {e}")
                self.aguardar_enter()

    def gerenciar_pedido_aberto(self):
        self.exibir_cabecalho("GERENCIAR PEDIDO ABERTO")
        
        if not self.pedidos_abertos:
            print("Nenhum pedido aberto no momento.")
            self.aguardar_enter()
            return
        
        print("Pedidos abertos:")
        for i, pedido in enumerate(self.pedidos_abertos, 1):
            print(f"{i}. Pedido #{pedido.id_pedido} - {pedido.cliente.nome} - R$ {pedido.calcular_valor_total():.2f}")
        
        try:
            opcao = int(input("\nSelecione o pedido (número): "))
            if 1 <= opcao <= len(self.pedidos_abertos):
                pedido = self.pedidos_abertos[opcao - 1]
                self.menu_gerenciar_pedido(pedido)
            else:
                print("Opção inválida!")
                self.aguardar_enter()
        except ValueError:
            print("Digite um número válido!")
            self.aguardar_enter()

    def menu_gerenciar_pedido(self, pedido):
        while True:
            self.exibir_cabecalho(f"GERENCIAR PEDIDO #{pedido.id_pedido}")
            print(f"Cliente: {pedido.cliente.nome}")
            print(f"Status: {pedido.status}")
            print(f"Valor atual: R$ {pedido.calcular_valor_total():.2f}")
            print("\nItens no pedido:")
            if pedido.itens:
                for item in pedido.itens:
                    print(f"  - {item}")
            else:
                print("  Nenhum item adicionado")
            
            print("\nOpções:")
            print("1. Adicionar produto")
            print("2. Remover produto")
            print("3. Ver resumo do pedido")
            print("0. Voltar")
            
            opcao = input("\nDigite a opção: ")
            
            if opcao == "1":
                self.adicionar_produtos_pedido(pedido)
            elif opcao == "2":
                self.remover_produto_pedido(pedido)
            elif opcao == "3":
                self.exibir_resumo_pedido(pedido)
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")
                self.aguardar_enter()

    def remover_produto_pedido(self, pedido):
        self.exibir_cabecalho(f"REMOVER PRODUTO - PEDIDO #{pedido.id_pedido}")
        
        if not pedido.itens:
            print("Nenhum produto no pedido para remover.")
            self.aguardar_enter()
            return
        
        print("Produtos no pedido:")
        for i, item in enumerate(pedido.itens, 1):
            print(f"{i}. {item.produto.nome} - {item.quantidade} m³")
        
        try:
            opcao = int(input("\nSelecione o produto para remover (número): "))
            if 1 <= opcao <= len(pedido.itens):
                produto_a_remover = pedido.itens[opcao - 1].produto
                pedido.remover_produto(produto_a_remover)
            else:
                print("Opção inválida!")
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
        
        self.aguardar_enter()

    def exibir_resumo_pedido(self, pedido):
        self.exibir_cabecalho(f"RESUMO PEDIDO #{pedido.id_pedido}")
        print(pedido)
        self.aguardar_enter()

    def fechar_pedido(self):
        self.exibir_cabecalho("FECHAR PEDIDO")
        
        if not self.pedidos_abertos:
            print("Nenhum pedido aberto para fechar.")
            self.aguardar_enter()
            return
        
        print("Pedidos abertos:")
        for i, pedido in enumerate(self.pedidos_abertos, 1):
            print(f"{i}. Pedido #{pedido.id_pedido} - {pedido.cliente.nome} - R$ {pedido.calcular_valor_total():.2f}")
        
        try:
            opcao = int(input("\nSelecione o pedido para fechar (número): "))
            if 1 <= opcao <= len(self.pedidos_abertos):
                pedido = self.pedidos_abertos[opcao - 1]
                
                if not pedido.itens:
                    print("Não é possível fechar um pedido sem itens!")
                    self.aguardar_enter()
                    return
                
                # Exibir resumo antes de fechar
                self.exibir_cabecalho("CONFIRMAR FECHAMENTO DO PEDIDO")
                print(pedido)
                
                confirmacao = input("\nConfirmar fechamento do pedido? (S/N): ").upper()
                if confirmacao == "S":
                    pedido.fechar_pedido()
                    self.pedidos_abertos.remove(pedido)
                    self.pedidos_fechados.append(pedido)
                    
                    # Exibir resumo final
                    print("\n" + "="*50)
                    print("PEDIDO FECHADO COM SUCESSO!")
                    print("="*50)
                    print(pedido)
                    
                else:
                    print("Fechamento cancelado.")
                    
            else:
                print("Opção inválida!")
                
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
        
        self.aguardar_enter()

    def listar_pedidos_fechados(self):
        self.exibir_cabecalho("PEDIDOS FECHADOS")
        
        if not self.pedidos_fechados:
            print("Nenhum pedido fechado.")
        else:
            for pedido in self.pedidos_fechados:
                print(pedido)
                print("-" * 50)
        
        self.aguardar_enter()

    def sair_sistema(self):
        self.exibir_cabecalho("SAIR DO SISTEMA")
        
        if self.pedidos_abertos:
            print("Atenção! Existem pedidos abertos:")
            for pedido in self.pedidos_abertos:
                print(f"  - Pedido #{pedido.id_pedido} - {pedido.cliente.nome}")
            print("\nRecomenda-se fechar os pedidos antes de sair.")
        
        confirmacao = input("\nDeseja realmente sair? (S/N): ").upper()
        if confirmacao == "S":
            print("\nObrigado por usar o sistema!")
            sys.exit(0)
        else:
            print("Retornando ao menu principal...")
            self.aguardar_enter()

def main():
    try:
        menu = MenuSistema()
        menu.menu_principal()
    except KeyboardInterrupt:
        print("\n\nSistema interrompido pelo usuário.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
        input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()