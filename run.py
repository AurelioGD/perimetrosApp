from os import system
from Formulas import Formulas
from Vistas import Vistas

formulas = Formulas()
vistas = Vistas()

def AreaCuadrado():
    system("cls")
    lado = vistas.drawValue("lado")
    area = formulas.ObtenerAreaCuadrado(lado)
    while True:
        vistas.drawArea("cuadrado", area)
        choice = vistas.drawSubmenu()
        if int(choice) < 1 or int(choice) > 2:
                system("cls")
                vistas.drawError("Opcion invalida, ingresa un valor del 1 al 2.")
                continue
        return choice

def PerimetroCuadrado():
    system("cls")
    lado = vistas.drawValue("lado")
    perimetro = formulas.ObtenerPerimetroCuadrado(lado)
    while True:
        vistas.drawPerimetro("cuadrado", perimetro)
        choice = vistas.drawSubmenu()
        if int(choice) < 1 or int(choice) > 2:
                system("cls")
                vistas.drawError("Opcion invalida, ingresa un valor del 1 al 2.")
                continue
        return choice
def AreaCirculo():
    system("cls")
    radio = vistas.drawValue("radio")
    area = formulas.ObtenerAreaCirculo(radio)
    while True:
        vistas.drawArea("circulo", area)
        choice = vistas.drawSubmenu()
        if int(choice) < 1 or int(choice) > 2:
                system("cls")
                vistas.drawError("Opcion invalida, ingresa un valor del 1 al 2.")
                continue
        return choice
def PerimetroCirculo():
    system("cls")
    radio = vistas.drawValue("radio")
    perimetro = formulas.ObtenerPerimetroCirculo(radio)
    while True:
        vistas.drawPerimetro("circulo", perimetro)
        choice = vistas.drawSubmenu()
        if int(choice) < 1 or int(choice) > 2:
                system("cls")
                vistas.drawError("Opcion invalida, ingresa un valor del 1 al 2.")
                continue
        return choice
def AreaTriangulo():
    system("cls")
    base = vistas.drawValue("base")
    height = vistas.drawValue("altura")
    perimetro = formulas.ObtenerAreaTriangulo(base, height)
    while True:
        vistas.drawArea("triangulo", perimetro)
        choice = vistas.drawSubmenu()
        if int(choice) < 1 or int(choice) > 2:
                system("cls")
                vistas.drawError("Opcion invalida, ingresa un valor del 1 al 2.")
                continue
        return choice
def PerimetroTriangulo():
    system("cls")
    lado = vistas.drawValue("lado")
    perimetro = formulas.ObtenerPerimetroTriangulo(lado)
    while True:
        vistas.drawPerimetro("triangulo", perimetro)
        choice = vistas.drawSubmenu()
        if int(choice) < 1 or int(choice) > 2:
                system("cls")
                vistas.drawError("Opcion invalida, ingresa un valor del 1 al 2.")
                continue
        return choice
def AreaHexagono():
    system("cls")
    lado = vistas.drawValue("lado")
    apotema = vistas.drawValue("apotema")
    area = formulas.ObtenerAreaHexagono(lado, apotema)
    while True:
        vistas.drawArea("hexagono", area)
        choice = vistas.drawSubmenu()
        if int(choice) < 1 or int(choice) > 2:
                system("cls")
                vistas.drawError("Opcion invalida, ingresa un valor del 1 al 2.")
                continue
        return choice
def PerimetroHexagono():
    system("cls")
    lado = vistas.drawValue("lado")
    perimetro = formulas.ObtenerPerimetroHexagono(lado)
    while True:
        vistas.drawPerimetro("hexagono", perimetro)
        choice = vistas.drawSubmenu()
        if int(choice) < 1 or int(choice) > 2:
                system("cls")
                vistas.drawError("Opcion invalida, ingresa un valor del 1 al 2.")
                continue
        return choice
CHOICES = {
    "1": AreaCuadrado,
    "2": PerimetroCuadrado,
    "3": AreaCirculo,
    "4": PerimetroCirculo,
    "5": AreaTriangulo,
    "6": PerimetroTriangulo,
    "7": AreaHexagono,
    "8": PerimetroHexagono
}

def run():
    system("cls")
    seguir = True
    while(seguir):
        choice = vistas.drawMenu()
        if int(choice) == 9: 
            system("cls")
            break
        if int(choice) < 1 or int(choice) > 9:
            system("cls")
            vistas.drawError("Opcion invalida, ingresa un valor del 1 al 9.")
            continue
        continueExecution = CHOICES.get(choice)()
        system("cls")
        if(int(continueExecution) == 2): 
            seguir = False
        
run()