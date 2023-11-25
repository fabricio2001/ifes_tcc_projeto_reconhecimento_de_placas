# sudo apt update
# sudo apt install rpi.gpio-common

import RPi.GPIO as GPIO
import time

# Configurar o modo GPIO
GPIO.setmode(GPIO.BCM)

# Definir o número do pino onde o LED está conectado
LED_PIN = 18

# Configurar o pino como saída
GPIO.setup(LED_PIN, GPIO.OUT)

# Acender o LED
GPIO.output(LED_PIN, True)

# Deixar o LED aceso por 5 segundos
time.sleep(5)

# Apagar o LED
GPIO.output(LED_PIN, False)

# Limpar a configuração do pino
GPIO.cleanup()

###################################################################

# sudo apt install python3-gpiozero
from gpiozero import LED
from time import sleep

# Definir o número do pino onde o LED está conectado
led = LED(18)

# Acender o LED
led.on()

# Deixar o LED aceso por 5 segundos
sleep(5)

# Apagar o LED
led.off()

