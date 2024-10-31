from gpiozero import LED, Servo
from time import sleep

buzzer = LED(17)     # Pin del buzzer
led = LED(4)         # Pin del LED, reemplaza 4 con el pin que estés usando para el LED
servo = Servo(18)    # Pin del servo, reemplaza 18 con el pin GPIO que estés usando para el servo

while True:
    # Mueve el servo a 180 grados mientras suena el buzzer
    servo.max()       # Mueve el servo a la posición máxima (180 grados)

    for _ in range(3):  # Ajusta el número de parpadeos (en este caso, 7)
        buzzer.on()
        sleep(0.2)    # El buzzer permanece encendido 0.3 segundos
        buzzer.off()
        sleep(0.05)   # El buzzer se apaga 0.05 segundos entre parpadeos

    # Mueve el servo de regreso a 0 grados, apaga el buzzer y enciende el LED
    servo.min()       # Vuelve el servo a la posición mínima (0 grados)
    buzzer.off()      # Asegúrate de que el buzzer está apagado
    led.on()          # Enciende el LED 

    led.off()         # Apaga el LED
    sleep(1.5)          # Espera 2 segundos antes de repetir el ciclo
