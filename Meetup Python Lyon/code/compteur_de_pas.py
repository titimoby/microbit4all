# https://microbit-micropython.readthedocs.io/en/latest/
from microbit import *

nombre_de_pas = 0

while True:
    if accelerometer.was_gesture("shake"):
        # si une secousse est detectee c'est un nouveau pas
        nombre_de_pas = nombre_de_pas + 1
        display.show(str(nombre_de_pas))
    if button_a.is_pressed():
        # l'appui du bouton A permet de reinitialiser le compteur
        nombre_de_pas= 0
        display.show(str(nombre_de_pas))
    if button_b.is_pressed():
        # l'appui sur le bouton B permet l'affichage du compteur
        display.show(str(nombre_de_pas))
        
