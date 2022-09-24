class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#EXPLICAÇÃO COM EXEMPLO
#AGORA É POSSÍVEL UTILIZARMOS "NÓS" PARA ESTUDO, POIS A CLASSE CRIADA (NODE) É UM ESPAÇO NA MEMÓRIA QUE CONTÉM DUAS INFORMAÇÕES: NEXT E DATA
#DATA SERIA O ELEMENTO PRÓPRIO DAQUELE NÓ E O NEXT SERIA O PRÓXIMO NÓ EXISTENTE

# node1 = Node(5) #ATRIBUIMOS O VALOR 5 PARA SER UM NÓ
# print(f'Node1 data: {node1.data}') #ESTAMOS PEGANDO O VALOR DAQUELE NÓ
# print(f'Node1 next: {node1.next}') #ESTAMOS PEGANDO O VALOR DO PRÓXIMO NÓ QUE FOI INSERIDO DEPOIS DO 5

# #ENQUANTO NÃO DEFINIRMOS O OUTRO NÓ O node1.next NÃO RETORNARÁ NADA

# #DEFININDO O SEGUNDO NÓ

# node2 = Node(9)
# print(f'Node2 data: {node2.data}') #RETORNAR O VALOR DO PRÓPRIO NÓ
# print(f'Node2 next: {node2.next}') #RETORNA O VALOR DO PRÓXIMO NÓ, NÃO TEM VALOR ENTÃO NÃO RETORNA NADA

# #DEFININDO O PRÓXIMO NÓ

# node1.next = node2 #DEFINIDO QUE O PRÓXIMO NÓ DO NÓ 5 É O NÓ 9
# print(f"Node1's next: {node1.next.data}") #RETORNARÁ 9