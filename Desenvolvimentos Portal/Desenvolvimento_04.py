"""
Instruções do projeto
A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente! 
Dessa vez, eles precisam que você atualize o array de produtos. 
Agora, eles estão vendendo rímel ao invés de batons, e cremes hidratantes no lugar de loções. Além disso, ficaram sem delineadores, 
então precisam que você remova ele da lista de produtos. Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

Como desafio, adicione dois novos produtos da sua escolha à lista. 

Trabalhe esse código no Google Colab, e compartilhe o link do projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.   


Remover da lista: batons, loções, delineadores
Incluir na lista: Rímel, Creme hidratantes 
"""


def removeProduto(lista):
        produto = str(input("Informe o nome do produto para remover: \n"))
        contador = 0
        tamanho_lista = len(lista)
        print(tamanho_lista)
        for  i in range(len(lista)):
            if (lista[i] == produto):
               lista.pop(i)
               print("Foi removido o produto: ", produto)
               return lista       
            



def altaraProdutos(lista):
    opcao = True
    while opcao == True:
        produto_descontinuado = input("Informe o nome do produto a ser alterado: \n")
        produto_novo = input("Informe o nome do novo produto: \n")

        for i in range(len(lista)):
            if lista[i] == produto_descontinuado :
                lista[i] = produto_novo
                print("Produto {lista[i]} foi alterado para o produto {produto_novo}.")
            else:
                print("Produto não encontrado")

        opcao1 = int(input("Alterar outro produto: 1-Sim 2-Não\n"))
        if opcao1 == 1:
           opcao = True
        else:
           opcao = False





    
#Chamada das funções
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 
print("Lista de Produtos Original: ", lista_produtos)
lista_produtos = removeProduto(lista_produtos)
print("Lista de produtos após remoção de itens: ", lista_produtos)



print(lista_produtos)
for i in range(len(lista_produtos)):
    if (lista_produtos[i] == "batons"):
        lista_produtos[i] = "rímel"
    elif lista_produtos[i] == "loções":
        lista_produtos[i] ="creme hidratante"
print(lista_produtos)
lista_produtos.pop()
print(lista_produtos)
opcao = True
while opcao == True:
    novo_produto = input("Novo produto a ser inserido na base de vendas:\n ")
    lista_produtos.append(novo_produto)
    opcao1 = int(input("Inserir novo produto: 1-Sim 2-Não\n"))
    if opcao1 == 1:
        opcao = True
    else:
        opcao = False

print(lista_produtos)
