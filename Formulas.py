from tokenize import Number


class Formulas:
    def __init__(self):
        self.PI = 3.1416
    def ObtenerPerimetroCirculo(self, radio):
        radioX2 = int(radio) + int(radio)
        perimetro = radioX2 * self.PI
        return perimetro
    def ObtenerAreaCirculo(self, radio):
        area = (int(radio) * int(radio)) * self.PI
        return area
    def ObtenerPerimetroCuadrado(self, lado):
        perimentro = int(lado) * 4
        return perimentro
    def ObtenerAreaCuadrado(self, lado):
        area = int(lado) * int(lado)
        return area
    def ObtenerPerimetroTriangulo(self, lado):
        perimentro = int(lado) * 3
        return perimentro
    def ObtenerAreaTriangulo(self, base, height):
        area = int(base) * int(height) / 2
        return area
    def ObtenerPerimetroHexagono(self, lado):
        perimentro = int(lado) * 6
        return perimentro
    def ObtenerAreaHexagono(self, lado, apotema):
        perimetro = self.ObtenerPerimetroHexagono(lado)
        area = perimetro * int(apotema) / 2
        return area

