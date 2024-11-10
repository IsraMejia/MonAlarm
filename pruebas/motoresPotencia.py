from gpiozero import OutputDevice, PWMOutputDevice
from time import sleep

class MotoresP:
    def __init__(self, in1_pin, in2_pin, enable_pin):
        # Configurar los pines GPIO para controlar el motor y el pin de habilitación
        self.in1 = OutputDevice(in1_pin)
        self.in2 = OutputDevice(in2_pin)
        self.enable = PWMOutputDevice(enable_pin)  # Usar PWM para control de velocidad
    
    def girar_adelante(self, potencia=1.0):
        """Gira el motor en sentido hacia adelante con la potencia especificada."""
        self.enable.value = potencia  # Establece la potencia (0 a 1)
        self.in1.on()
        self.in2.off()
        print(f"Motor en marcha hacia adelante a {int(potencia * 100)}% de potencia...")
        
    def girar_atras(self, potencia=1.0):
        """Gira el motor en sentido hacia atrás con la potencia especificada."""
        self.enable.value = potencia  # Establece la potencia (0 a 1)
        self.in1.off()
        self.in2.on()
        print(f"Motor en marcha hacia atrás a {int(potencia * 100)}% de potencia...")
        
    def detener(self):
        """Detiene y deshabilita el motor."""
        self.in1.off()
        self.in2.off()
        self.enable.off()
        print("Motor detenido y deshabilitado.")



# Ejemplo de uso
ventilador = MotoresP(in1_pin=20, in2_pin=21, enable_pin=16)
dispensador_agua = MotoresP(in1_pin=19, in2_pin=26, enable_pin=13)

# Bucle para controlar el motor desde el terminal
while True:
    mensaje = "Ingrese :\n\t'A' para girar adelante, \n\t'R' para girar atrás, \n\t'S' para detener y salir. \n\t'W' Servir water \n\t'D' devolver awa \nTecla ingresada:  "
    comando = input(mensaje).upper() 
    
    if comando == "A":
        ventilador.girar_adelante(potencia=0.6)  # Ejecuta a la mitad de la potencia
        sleep(15)
        ventilador.detener()
        
    elif comando == "R":
        ventilador.girar_atras(potencia=0.7)  # Ejecuta a la mitad de la potencia
        sleep(10)
        ventilador.detener()

    if comando == "W":
        print('Sirviendo awa')
        dispensador_agua.girar_adelante(potencia=0.9)  # Ejecuta a la mitad de la potencia
        sleep(10)
        dispensador_agua.detener()
        
    elif comando == "D":
        print('devolviendo awa')
        dispensador_agua.girar_atras(potencia=0.9)  # Ejecuta a la mitad de la potencia
        sleep(3)
        dispensador_agua.detener()
        
    elif comando == "S":
        ventilador.detener()
        dispensador_agua.detener()
        print("Saliendo...")
        break
    
    else:
        print("Comando no reconocido. Intente de nuevo.")
