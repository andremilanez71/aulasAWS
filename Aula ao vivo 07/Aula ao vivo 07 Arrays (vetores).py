"""
Permitir que o usuário interaja com o usuário.
mostrar o indice do elemento.  

"""


opcao = True
nomes = ["Andre", "Felipe","Luis", "Ricardo", "Diandra", "Jeff"]

#Funções
def acharElemento(elemento, arr ):
    achou = False
    for i in range(len(arr)):
        if (arr[i] == elemento):
            achou = True
            posicao = i

    if (achou == False):
        print("Não achamos o elemento: ", elemento)
    else:
        print("Encontramos o elemento: ", elemento, "no indice ", posicao)    
    

#Principal

ele = str(input("Informe o nome do elemento procurado: \n"))
acharElemento(ele,nomes)        

while opcao == True:
    opcao1 = int(input("Deseja encontrar outro elemento? 1-Sim 2-Não\n"))
    if (opcao1 == 1):
        ele = str(input("Informe o nome do elemento procurado: \n"))
        acharElemento(ele,nomes)        
    else:
        opcao = False


"""

"""








