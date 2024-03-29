class Printer:
    def char(self, n, c):
        print("Integer: ", n)
        print("Character: ", c)

    def int(self, c, n):
        print("Character: ", c)
        print("Integer: ", n)


a = Printer()
a.char(10, "N")
a.int("I", 20)
