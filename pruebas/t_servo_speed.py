from gpiozero import LED, Servo
from time import sleep

servo1 = Servo(18)    # Pin del servo, reemplaza 18 con el pin GPIO que estés usando para el servo
servo2 = Servo(19)
speed = 0.2

while True:
    # Mueve el servo a 180 grados mientras suena el buzzer
    #servo1.on()
    servo1.max()       # Mueve el servo a la posición máxima (180 grados)
    sleep(speed) 

    # Mueve el servo de regreso a 0 grados, apaga el buzzer y enciende el LED
    servo1.min()       # Vuelve el servo a la posición mínima (0 grados)
 
    sleep(speed)          # Espera 2 segundos antes de repetir el ciclo
    #servo1.off() 
    sleep(0.3)
