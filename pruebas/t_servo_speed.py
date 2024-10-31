from gpiozero import LED, Servo
from time import sleep

buzzer = LED(17)  # Pin del buzzer
servo1 = Servo(18)    # Pin del servo, reemplaza 18 con el pin GPIO que estés usando para el servo
servo2 = Servo(19)

speed = 0.3


gorila_mov =0
while gorila_mov < 4: 
    buzzer.on()
    servo1.max()       # Mueve el servo a la posición máxima (180 grados)
    sleep(speed)  
    servo1.min()       # Vuelve el servo a la posición mínima (0 grados) 
    buzzer.off()
    sleep(speed)   
    
    gorila_mov = gorila_mov+ 1

servo1.stop()

