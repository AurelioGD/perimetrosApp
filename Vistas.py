class Vistas: 
    def drawMenu(self):
        print("Aplicacion de figuras")
        print("1.-Obtener area del cuadrado")
        print("2.-Obtener perimetro del cuadrado")
        print("3.-Obtener area del circulo")
        print("4.-Obtener perimetro del circulo")
        print("5.-Obtener area del triangulo")
        print("6.-Obtener perimetro del triangulo")
        print("7.-Obtener area del hexagono")
        print("8.-Obtener perimetro del hexagono")
        print("9.-Salir")
        choice = input("Elige una opcion: ")
        return choice
    def drawSubmenu(self):
        print("1.-Continuar")
        print("2.-Ni de coña chaval!")
        choice = input("Elige una opcion: ")
        return choice
    def drawValue(self, measure):
        value = input(f"Introduce el {measure}: ")
        return value
    def drawPerimetro(self, figure, perimetro):
        print(f"El perimetro del {figure} es: {perimetro}")
    def drawArea(self, figure, area):
        print(f"El area del {figure} es: {area}")
    def drawError(self,message):
        print(message)