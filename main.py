class Asiento:
    def __init__(self, color, precio, registro):
       self.color = color
       self.precio = precio
       self.registro = registro

    def cambiarColor(self, color):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores:
            self.color = color

class Auto:
    cantidadCreados = 200
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        

    def cantidadAsientos(self):
        return len(self.asientos)

    def verificarIntegridad(self):    
        flag = False
        for element in self.asientos:
            if((element.registro != self.registro) or (element.registro != self.motor.registro) or (self.registro != self.motor.registro)):
                flag = True
        if(flag):
            return "Las piezas no son originales"
        else:
            return "Auto Original"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        self.tipo = tipo        



        