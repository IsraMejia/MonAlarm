# Instalación del gpio
# sudo apt update && sudo apt upgrade python3-gpiozero

from gpiozero import LED
from time import sleep

buzzer = LED(17)  # Pin del buzzer
led = LED(4)    # Pin del LED, reemplaza 17 con el pin que estés usando para el LED

while True:
    led.on()  # Enciende el LED
    # Hacemos que el buzzer parpadee mientras el LED está encendido
    for _ in range(7):  # Ajustamos el número de parpadeos (aquí serán 10 en 1 segundo)
        buzzer.on()
        sleep(0.3)      # El buzzer se mantiene encendido por 0.05 segundos
        buzzer.off()
        sleep(0.05)      # El buzzer se apaga por 0.05 segundos
    

    led.off()  # Apaga el LED
    sleep(2)   # Espera 2 segundos antes de repetir el ciclo
