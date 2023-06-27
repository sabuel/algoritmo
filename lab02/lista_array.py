from estrutura_elementar import estrutura_elementar


class ArrayList(estrutura_elementar):
    def __init__(self):
        self.lista = []

    def esta_vazio(self) -> bool:
        if(len(self.lista) == 0):
            return True
        return False

    def inserir(self, item):
        self.lista.append(item)

    def remove(self, item):
        if(len(self.lista) > 0):
            contador = 0
            for i in self.lista:           
                if(i == item):
                    self.lista.pop(contador)
                contador +=1
        pass

    def tamanho(self) -> int:
        return len(self.lista)

    def limpa(self):
        self.lista.clear()

    def procura(self, item) -> bool:
        for i in self.lista:
            if (i == item):
                return True
        return False

    def indice_de(self, item):
        for i in range(len(self.lista)):
            if(self.lista[i] == item):
                return i
        return -1

    def recupera_indice(self, index):
        if(len(self.lista) == 0 or index > (len(self.lista) - 1)):
            return None
        return self.lista[index]
