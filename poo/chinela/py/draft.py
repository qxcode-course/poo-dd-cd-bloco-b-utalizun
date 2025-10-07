class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, valor: int ):
        
        if valor > 19 and valor < 51 and valor % 2 == 0:
            self.__tamanho = valor
            print('Ótima escolha!\n')
            return
        
        print('tamanho errado, tente outro valor \n')

havaianas = Chinela()

while havaianas.getTamanho() == 0:
    print("Digite o tamanho da chinela:")
    size = int(input())
    havaianas.setTamanho(size)

print ("\nOpa cumpade tu comprou uma chinela tamanho: ", havaianas.getTamanho(),"\n")