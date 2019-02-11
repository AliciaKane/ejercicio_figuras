class Figura ():

    def Perimetro(self):
        return "Esta figura no tiene area"

    def Perimetro(self):
        return "Esta figura no tiene perimetro"

class Rectangulo(Figura):
    def __init__(self, arg1, arg2):
        #super(Rectangulo, self).__init__()
        self.base = arg1
        self.altura = arg2

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2*self.base + 2*self.altura


figura = Rectangulo(3,5)
print(figura.area())
