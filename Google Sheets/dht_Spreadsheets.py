import time
import datetime
import board
import adafruit_dht
import sys 

time = datetime.datetime.now()
from time import sleep

import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D18)
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

GDOCS_OAUTH_JSON       = 'pythonsensor-350114.json'

# Google Docs spreadsheet name.
GDOCS_SPREADSHEET_NAME = 'Dht22'

# How long to wait (in seconds) between measurements.
FREQUENCY_SECONDS      = 5


def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    try:
        scope =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1 # pylint: disable=redefined-outer-name
        return worksheet
    except Exception as ex: # pylint: disable=bare-except, broad-except
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, \
        and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)
        print('Logging sensor measurements to\
 {0} every {} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
print('Press Ctrl-C to quit.')
worksheet = None
worksheet = None
while True:
    try:
        time_now = datetime.datetime.now()
        # Print the values to the serial port
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(time_now.strftime("%a %d %b - %X"))
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity,
        worksheet.append_row((time_now.strftime("%a %d %b - %X"), temperature_c, temperature_f, humidity))
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
