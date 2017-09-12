from microbit import display, Image, sleep
import radio
radio.on()
radio.config(channel=7)

while True:
    msgin = radio.receive()

    if msgin == 'f':
        display.show(Image.ARROW_N)
        sleep(100)

    elif msgin == 'b':
        display.show(Image.ARROW_S)
        sleep(100)

    elif msgin == 'l':
        display.show(Image.ARROW_W)
        sleep(100)

    elif msgin == 'r':
        display.show(Image.ARROW_E)
        sleep(100)

    else:
        display.show("-")
        sleep(100)
