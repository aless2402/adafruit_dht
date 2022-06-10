# Adafruit_dht AM2303 / DHT22

***

![dht22](https://user-images.githubusercontent.com/48935269/173150976-058744a2-5b65-48e4-b7f7-427de7aaa99e.jpg)
![cabñe](https://user-images.githubusercontent.com/48935269/173151043-676cc592-f2e7-4cd2-894e-c96a317181cd.png)
![raspberryp4](https://user-images.githubusercontent.com/48935269/173151058-13199dd2-7fbb-43a9-94c1-ece9732538fb.png)


## Install python raspberry pi 4 library packages

```
apt-get sudo upgrade
apt-get sudo update

pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2
sudo apt-get install build-essential python-dev
```

## import the  libraries for editors

````
import adafruit_dht
````
````
import board
import time
````

## your the device for dht22 or dht11 on sensors board

````
#Initial the dht device, with data pin connected to:
#dhtDevice = adafruit_dht.DHT22(board.D18)
#you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
#This may be necessary on a Linux single board computer like the Raspberry Pi,
#but it will not work in CircuitPython.
````
## I use pin 4 the sensor dht22 from board
````
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
````

### perform the one where the temperature and humidity are placed to connect in While True power that allow to read the temperature


    while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
 
        
        
### print every second of read read al must be connected from adafruit_dht to DHT22 sensor
 `````` 
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        #print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    except KeyboardInterrupt:
        dhtDevice.exit()
        print('exiting script')
    time.sleep(2.0)
``````
