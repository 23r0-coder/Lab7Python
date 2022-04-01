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
        time.sleep(0.1)
        if (analog_value >= 0.500):
            led.write(1)
        else:
            led.write(0)