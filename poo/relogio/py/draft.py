class Relogio:
    def __init__(self):
        self.__hora = 0
        self.__min = 0
        self.__seg = 0

    def get_hora(self) -> int:
        return self.__hora

    def get_min(self) -> int:
        return self.__min

    def get_seg(self) -> int:
        return self.__seg

    def set_hora(self, valor: int):
        if 0 <= valor < 24:
            self.__hora = valor
        else:
            print("fail: hora invalida")

    def set_min(self, valor: int):
        if 0 <= valor < 60:
            self.__min = valor
        else:
            print("fail: minuto invalido")

    def set_seg(self, valor: int):
        if 0 <= valor < 60:
            self.__seg = valor
        else:
            print("fail: segundo invalido")

    def init(self, h: int, m: int, s: int):
        self.__hora = 0
        self.__min = 0
        self.__seg = 0
        if not (0 <= h < 24):
            print("fail: hora invalida")
        else:
            self.__hora = h
        if not (0 <= m < 60):
            print("fail: minuto invalido")
        else:
            self.__min = m
        if not (0 <= s < 60):
            print("fail: segundo invalido")
        else:
            self.__seg = s

    def nextSecond(self):
        self.__seg += 1
        if self.__seg > 59:
            self.__seg = 0
            self.__min += 1
        if self.__min > 59:
            self.__min = 0
            self.__hora += 1
        if self.__hora > 23:
            self.__hora = 0

    def __str__(self) -> str:
        return f"{self.__hora:02}:{self.__min:02}:{self.__seg:02}"


def main():
    time = Relogio()
    while True:
        try:
            line: str = input()
        except EOFError:
            break
        if not line.strip():
            continue
        print("$" + line)
        args = line.split()
        cmd = args[0]
        if cmd == "end":
            break
        elif cmd == "show":
            print(time)
        elif cmd == "set":
            if len(args) != 4:
                print("fail: use 'set hora min seg'")
                continue
            try:
                hora = int(args[1])
                minuto = int(args[2])
                seg = int(args[3])
                time.set_hora(hora)
                time.set_min(minuto)
                time.set_seg(seg)
            except ValueError:
                print("fail: argumentos devem ser inteiros")
        elif cmd == "init":
            if len(args) != 4:
                print("fail: use 'init hora min seg'")
                continue
            try:
                h = int(args[1])
                m = int(args[2])
                s = int(args[3])
                time.init(h, m, s)
            except ValueError:
                print("fail: argumentos devem ser inteiros")
        elif cmd == "next":
            time.nextSecond()
        else:
            print("fail: comando invalido")


if __name__ == "__main__":
    main()
