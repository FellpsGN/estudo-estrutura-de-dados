from node import Node
class LinkedList:
    def __init__(self):
        self.head = None #VALOR INICIAL, PRIMEIRO VALOR INSERIDO
        self._size = 0 #TAMANHO DA LISTA

    def append(self, element): #ADICIONAR VALORES NA LISTA ENCADEADA
        
        if self.head:
            #INSERÇÃO DE ELEMENTOS QUANDO A LISTA HÁ UM ELEMENTO
            pointer = self.head #self.head possui next pois quando inserido o primeiro elemento definimos ele como um Node
            while pointer.next != None: #CONFERINDO SE CHEGOU AO FINAL DA LISTA, ENQUANTO EXISTIR UM NEXT
                pointer = pointer.next #PROCURANDO O ÚLTIMO ELEMENTO OU ÚLTIMO NÓ
            pointer.next = Node(element) #SE ELE ENCONTROU O ÚLTIMO NÓ ELE SAI DO WHILE E ADICIONA O NEXT DESSE ÚLTIMO NÓ INSERIDO
            self._size += 1
        else:
            #PRIMEIRA INSERÇÃO // FIRST INSERTION
            self.head = Node(element)
            self._size += 1  #OU self.size = self.size + 1

    def __len__(self):
        #RETORNA O TAMANHO DA LISTA
        return self._size

    #def get(self, index):

    def __setitem__(self, index, element):
        pointer = self.head

        for i in range(index): #ESSE FOR IRÁ ANDAR ATÉ O NÚMERO QUE VOCÊ QUER
            if pointer != None: #SE O POINTER NÃO FOR NONE
                pointer = pointer.next 
            else:
                raise IndexError("list index out of range") #SE O POINTER FOR NONE, APRESENTE UM ERRO
        if pointer: #SE O POINTER NÃO FOR NONE 
            pointer.data = element
        raise IndexError("list index out of range") #SE O POINTER FOR NONE

    def __getitem__(self, index):
        pointer = self.head

        for i in range(index): #ESSE FOR IRÁ ANDAR ATÉ O NÚMERO QUE VOCÊ QUER
            if pointer != None: #SE O POINTER NÃO FOR NONE
                pointer = pointer.next 
            else:
                raise IndexError("list index out of range") #SE O POINTER FOR NONE, APRESENTE UM ERRO
        if pointer: #SE O POINTER NÃO FOR NONE 
            return pointer.data
        else:
            raise IndexError("list index out of range") #SE O POINTER FOR NONE

    def index(self, element):
        pointer, i = self.head, 0
        while pointer:
            if pointer.data == element:
                return i
            pointer, i = pointer.next, (i+1)
        raise ValueError(f"{element} is not in list")
            

lista = LinkedList()
lista.append(7)
print(len(lista))
lista.append(80)
print(len(lista))

print(lista[0])
print(lista[1])

print(lista.index(80))
print(lista.index(4))