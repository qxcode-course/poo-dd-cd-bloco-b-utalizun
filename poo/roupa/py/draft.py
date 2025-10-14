class Roupa:
    def __init__(self):
        self.__tamanho = ""
    
    def get_tamanho(self)-> str:
        return self.__tamanho
    
    def set_tamanho(self, valor: str):
        tamanhos_validos = ["PP","P","M","G","GG","XG"]
        valor_upper = valor.upper()
        if valor_upper in tamanhos_validos:
            self.__tamanho = valor_upper
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
       
    def __str__(self):
        return f"size: ({self.__tamanho})"
    

def main():
    camisa = Roupa()
    while True: #loop infinito 
        line: str = input()
        print ("$"+line)
        args: list[str]=line.split(" ")

        if args[0] == "end":
            break
        
        elif args[0] == "show":
            print(camisa)

        elif args[0] == "size":
            if len(args) > 1 or len(args) <=2: 
                size = args[1]
                camisa.set_tamanho(size)
            else:
                print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

if __name__ == "__main__":
    main()