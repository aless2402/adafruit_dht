import time
import datetime
import board
import adafruit_dht

time = datetime.datetime.now()
from time import sleep
# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D18)
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
while True:
    try:
        time_now = datetime.datetime.now()
        # Print the values to the serial port
        
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(time_now.strftime("%a %d %b - %X"))
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity,
            )
            
        )
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        # print(error.args[0])
        sleep(5)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    except KeyboardInterrupt:
        dhtDevice.exit()
        
    sleep(5)
