from gpiozero import LED, Servo
from time import sleep

class Gorila:
    def __init__(self, buzzer_pin, servo1_pin, servo2_pin, speed=0.3):
        self.buzzer = LED(buzzer_pin)  # Pin del buzzer
        self.servo1 = Servo(servo1_pin)  # Pin del servo 1
        self.servo2 = Servo(servo2_pin)  # Pin del servo 2
        self.speed = speed

    def g_angry(self):
        print('haz hecho enojar al gorila')
        gorila_mov = 0
        while gorila_mov < 4: 
            #self.buzzer.on()
            self.servo1.max()  # Mueve el servo a la posición máxima (180 grados)
            sleep(self.speed)  
            self.servo1.min()  # Vuelve el servo a la posición mínima (0 grados) 
            self.buzzer.off()
            sleep(self.speed)   
            
            gorila_mov += 1

        #self.servo1.stop()
        print('el gorila te observa')

# Ejemplo de uso
gorila = Gorila(buzzer_pin=17, servo1_pin=18, servo2_pin=19)
gorila.g_angry()
sleep(3)
print('se durmio el gorilon')
gorila.g_angry()


