from node import Node
class LinkedList:
    def __init__(self):
        self.head = None #VALOR INICIAL, PRIMEIRO VALOR INSERIDO
        self._size = 0 #TAMANHO DA LISTA

    def append(self, element): #ADICIONAR VALORES NA LISTA ENCADEADA
        
        if self.head:
            #INSERÇÃO DE ELEMENTOS QUANDO A LISTA HÁ UM ELEMENTO
            pointer = self.head #self.head possui next pois quando inserido o primeiro elemento definimos ele como um Node
            
            #MELHOR CASO É INSERIR APENAS UM ELEMENTO // PIOR CASO É INSERIR N ELEMENTOS EM UMA LISTA QUE JÁ CONTÉM ELEMENTOS, POIS IRÁ PERCORRER TODA A LISTA, "N" ELEMENTOS, PARA ADICIONAR O NOVO ELEMENTO-> O(N)
            
            while pointer.next != None: #CONFERINDO SE CHEGOU AO FINAL DA LISTA, ENQUANTO EXISTIR UM NEXT
                pointer = pointer.next #PROCURANDO O ÚLTIMO ELEMENTO OU ÚLTIMO NÓ
            pointer.next = Node(element) #SE ELE ENCONTROU O ÚLTIMO NÓ ELE SAI DO WHILE E ADICIONA O NEXT DESSE ÚLTIMO NÓ INSERIDO
            self._size += 1
        else:
            #PRIMEIRA INSERÇÃO // FIRST INSERTION
            self.head = Node(element) 
            self._size += 1  #OU self.size = self.size + 1

    def __len__(self):
        #RETORNA O TAMANHO DA LISTA O(1)
        return self._size

    def _getnode(self, index):
        pointer = self.head

        for i in range(index): #ESSE FOR IRÁ ANDAR ATÉ O NÚMERO QUE VOCÊ QUER O(n)
            if pointer != None: #SE O POINTER NÃO FOR NONE
                pointer = pointer.next 
            else:
                raise IndexError("list index out of range") #SE O POINTER FOR NONE, APRESENTE UM ERRO
        return pointer 

    def __setitem__(self, index, element): #O(N)
        pointer = self._getnode(index)
        if pointer: #SE O POINTER NÃO FOR NONE 
            pointer.data = element
        raise IndexError("list index out of range") #SE O POINTER FOR NONE

    def __getitem__(self, index): #O(N)
        pointer = self._getnode(index)
        if pointer: #SE O POINTER NÃO FOR NONE 
            return pointer.data
        else:
            raise IndexError("list index out of range") #SE O POINTER FOR NONE

    def index(self, element):
        pointer, i = self.head, 0
        while pointer: # O(n) -> Pode querer pegar o último elemento, e com isso teria que percorrer a lista toda
            if pointer.data == element:
                return i
            pointer, i = pointer.next, (i+1)
        raise ValueError(f"{element} is not in list")

    def insert(self, index, element):
        node = Node(element) #O ELEMENTO INSERIDO SE TORNARÁ UM NÓ
        if index == 0: #SE A PESSOA INSERIR NA CABEÇA DA LISTA, 
            
            node.next = self.head #O PRÓXIMO NÓ DESSE ELEMENTO VAI SER O QUE ESTÁ NA SELF.HEAD
            self.head = node #E O SELF.HEAD PASSA A SER O NÓ QUE A PESSOA INSERIU (ELEMENT)
        else:
            #SUPONDO QUE A LISTA SEJA: [0,2,5,6]
            #E QUEREMOS INSERIR NA POSIÇÃO 2, QUE SERIA NO LUGAR NO 5 (NÃO SERIA SUBSTITUIR O 5, SERIA APENAS MODIFICAR POSIÇÃO)
            pointer = self._getnode(index-1) #PEGANDO O NÓ ANTERIOR ÀQUELE QUE EU QUERO INSERIR ENTÃO PEGAMOS O NÚMERO DA POSIÇÃO 1 QUE SERIA O 2 DA LISTA
            #node = Node(element) #CRIAÇÃO DO NOVO NÓ, SUPONDO QUE QUEREMOS COLOCAR O NÚMERO 4
            node.next = pointer.next #O PRÓXIMO NÓ DO NOSSO NOVO NÓ SERÁ O 5, POIS O POINTER ESTÁ NA POSIÇÃO 1 E O PRÓXIMO DA POSIÇÃO 1 SERIA O NÚMERO 5
            pointer.next = node #TROCANDO O NEXT DO NÚMERO 2 QUE ERA O 5 PELO 4 QUE ESTAMOS INSERINDO
        self._size += 1
        
            

lista = LinkedList()
lista.append(0)
lista.append(2)
lista.append(5)
lista.append(6)
#print(len(lista))
#print(len(lista))

#print(lista[0])
#print(lista[1])

#print(lista.index(80))
#print(lista.index(4)) #Erro proposital para verificação da função index

lista.insert(2, 4)
print(lista[2])
print(lista[3])
print(lista[4])

lista.insert(len(lista), 27)
print(lista[len(lista)-1])
print(lista.index(27))
