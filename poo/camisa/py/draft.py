class Blusa:
    def __init__(self):
        self.__tam = " "
    def getTam(self) -> str:
        return self.__tam
    def setTam(self, valor: str):
        if valor == "pp" or valor == "p" or valor == "m" or valor == "g" or valor == "gg" or valor == "xg":
            self.__tam = valor
            print ("Ótima escolha!\n")
            return
        
        print("valor invalido")
            

camisa = Blusa()

while camisa.getTam() == " ":
    print("Digite o tamanho da camisa:")
    size = input()
    camisa.setTam(size)

print ("\nOpa cumpade tu comprou uma blusa tamanho: ", camisa.getTam(),"\n")