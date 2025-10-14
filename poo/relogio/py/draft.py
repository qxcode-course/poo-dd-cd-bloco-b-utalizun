class Relogio:
    def __init__(self):
        self.__hora = 0
        self.__min = 0
        self.__seg = 0

    def get_hora(self)-> int:
        return self.__hora
    def get_min(self)-> int:
        return self.__min
    def get_seg(self)-> int:
        return self.__seg
    
    def set_hora(self, valor: int):
        if valor > 23:
            print("fail: hora invalida")
        elif valor >=0 and valor <=23: 
            self.__hora = valor
    def set_min(self, valor: int):
        if valor > 59:
            print("fail: minuto invalido")
        elif valor >= 0 and valor <=59: 
            self.__min = valor
    def set_seg(self, valor: int):
        if valor > 59:
            print("fail: segundo invalido")
        elif valor >= 0 and valor <=59: 
            self.__seg = valor

    def __str__ (self) -> str:
        return f"{self.__hora:02}:{self.__min:02}:{self.__seg:02}"
    
def main():
    time = Relogio()
    while True: #loop infinito 
        line: str = input()
        print ("$"+line)
        args: list[str]=line.split(" ")

        if args[0] == "end":
            break
        elif args[0]=="show":
            print(time)
        elif args[0]=="set":
            if len(args) == 4: 
                hora = int(args[1])
                minuto = int(args[2])
                seg = int(args[3])
                time.set_hora(hora)
                time.set_min(minuto)
                time.set_seg(seg)
            
if __name__ == "__main__":
    main()
