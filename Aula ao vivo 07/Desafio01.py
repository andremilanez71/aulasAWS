"""

"""

estoque =["Cimento", "Areia"]
def main():
    try:
        global estoque
        print("Sistema de controle de estoque!")
        opcao = int(input("Escolha uma opção:\n1-Cadastrar Novo Produto\n2-Alterar Produto\n3-Remover Produto\n4-Imprimir Estoque\n5-Sair\n"))
        if (opcao >=1 and opcao<=5):
            match opcao:
                case 1:
                    opcao1 = True
                    while opcao1 == True:
                        print("Cadastro de produtos")
                        incluiEstoque()
                        opcao1 = continuar("Cadastro de Produtos")  
                    main()
                case 2:
                    opcao1 = True
                    while opcao1 == True:
                        print("Alteração de produtos")
                        alteraEstoque()
                        opcao1 = continuar("Alteração de Produto")  
                    main()
                    
                case 3:
                    opcao1 = True
                    while opcao1 == True:
                        print("Remoção de produtos")
                        removeEstoque()
                        opcao1 = continuar("Remoção de Produto ")  
                    main()
                    
                case 4:
                    print("Esse é nosso estoque ")
                    print("Indice  Descrição")
                    for i in range(len(estoque)):
                        print(" ", i,"   ",estoque[i])
                    main()
                case 5: 
                    print("Saindo do Sistema")
        else:
            print("Opcão inválida")
            main()            
    except:
        print("Opção inválida, tente novamente!")
        main()

def continuar(operacao):
    verifica = int(input("Deseja realizar uma nova operação de "+ str(operacao)+ "?\n 1-SIM\n 2-Não\n"))
    if (verifica == 1):
        return  True
    else: 
        return False

def incluiEstoque():
    try:
        estoque.append(input("Informe a descrição do novo produto?\n "))
        return 
    except:
        print("Produto Inválido")
    

def alteraEstoque():
    achou = False
    print("Esse é o estoque atual: ", estoque)
    produto_alteracao = input("Informe a descrição do produtoa ser alterado: \n")
    novo_produto = input("Informe a Descrição do novo produto: \n")
    for i in range(len(estoque)):
        if (produto_alteracao == estoque[i]):
            achou = True
            posicao = i

    if (achou == True):
        estoque[posicao] = novo_produto
    else:
        print("Produto não encontrado!")
        alteraEstoque()
    
           
def removeEstoque():
    try:
        achou = False
        print("Esse é o estoque atual: ",estoque)
        opcaor = int(input("Deseja informar o produto a ser removido ou remover o ultimo produto do estoque ?\n 1-Informar produto \n 2-Remover ultimo produto do estoque\n "))

        if (opcaor == 1):
            print
            produto_remocao = input("Informe a descrição do produto a ser removido: ")  
            for i in range(len(estoque)):
                if (produto_remocao == estoque[i]):
                    achou = True
                    posicao = i

            if (achou == True):
                estoque.pop(posicao)
            else:
                print("Produto não encontrador!")
                
        else:
            estoque.pop()
    except:
        print("Opcão inválida! tente novamente")
        removeEstoque()


#Chamado Função Principal
main()
