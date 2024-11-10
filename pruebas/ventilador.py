Te muestro como quedo el codigo con ligeras modificaciones.
Ahora quiero que agregues la logica para que gire a la mitad de la potencia maxima

from gpiozero import OutputDevice
from time import sleep

class VentiladorL298N:
    def __init__(self, in1_pin, in2_pin, enable_pin):
        # Configurar los pines GPIO para controlar el motor y el pin de habilitación
        self.in1 = OutputDevice(in1_pin)
        self.in2 = OutputDevice(in2_pin)
        self.enable = OutputDevice(enable_pin)
    
    def girar_adelante(self):
        """Gira el motor en sentido hacia adelante."""
        self.enable.on()
        self.in1.on() #Adelante
        self.in2.off()
        print("Motor en marcha hacia adelante...")
        
    def girar_atras(self):
        """Gira el motor en sentido hacia atrás."""
        self.enable.on()
        self.in1.off()
        self.in2.on() # Reversa
        print("Motor en marcha hacia atrás...")
        
    def detener(self):
        """Detiene y deshabilita el motor."""
        self.in1.off()
        self.in2.off()
        self.enable.off()
        print("Motor detenido y deshabilitado.")



# Ejemplo de uso
ventilador = VentiladorL298N(in1_pin=20, in2_pin=21, enable_pin=16)

# Bucle para controlar el motor desde el terminal
while True:
    comando = input("Ingrese 'A' para girar adelante, 'R' para girar atrás, o 'S' para detener y salir: ").upper()
    
    if comando == "A":
        ventilador.girar_adelante()
        sleep(5)
        ventilador.detener()
        
    elif comando == "R":
        ventilador.girar_atras()
        sleep(5)
        ventilador.detener()
        
    elif comando == "S":
        ventilador.detener()
        print("Saliendo...")
        break
    
    else:
        print("Comando no reconocido. Intente de nuevo.")
