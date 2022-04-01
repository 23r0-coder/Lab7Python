import pyfirmata
import time
 
board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()
 
analog_input = board.get_pin('a:0:i')
led = board.digital[13]

while True:
    analog_value = analog_input.read()
    if analog_value is not None:   
        led.write(1)
        time.sleep(0.1)
        if (analog_value >= 0.990):
            print("Baje la intensidad")
            led.write(1)
            time.sleep(0.5)
            led.write(0)
            time.sleep(0.5)
        else:
            led.write(1)