from microbit import display, Image, accelerometer, sleep
import radio
radio.on()
radio.config(channel=7)

while True:
    readingy = accelerometer.get_y()
    readingx = accelerometer.get_x()

    if readingy > 550:
        display.show(Image.ARROW_S)
        radio.send('b')
        sleep(100)

    elif readingy < -550:
        display.show(Image.ARROW_N)
        radio.send('f')
        sleep(100)

    elif readingx < -550:
        display.show(Image.ARROW_W)
        radio.send('l')
        sleep(100)

    elif readingx > 550:
        display.show(Image.ARROW_E)
        radio.send('r')
        sleep(100)

    else:
        display.show("-")
