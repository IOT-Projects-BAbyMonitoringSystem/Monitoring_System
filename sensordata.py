'''read the data from dht11 sensor and store it in the csv file '''
import csv
import time
#import adafruit_dht
import datetime
from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from flask import Flask, render_template, make_response
from random import random

# #Set GPIO sensor is connected to
# gpio1 = 3
# gpio2 = 2

# #Set sensor type : Options are DHT11,DHT22 or AM2302
# sensor1 = adafruit_dht.DHT11(gpio1)
# sensor2 = adafruit_dht.DHT11(gpio2)
# def read_sensor():
#     #Read the sensor
#     temp1 = sensor1.temperature
#     hum1 = sensor1.humidity
#     temp2 = sensor2.temperature
#     hum2 = sensor2.humidity
#     #calculate the precise temperature and humidity using mean and standard deviation
#     temp = (temp1 + temp2)/2
#     hum = (hum1 + hum2)/2
#     return temp, hum

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    temperature, humidity = random()*50, random()*40
        # date = datetime.datetime.now()
    # date = date.strftime("%/%m/%Y %H:%M:%S")
    # date = {'date': date}
     #read_sensor()
    data = [temperature, humidity]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


# def write_csv(temp, hum):
#     with open('dht11.csv', 'a') as csvfile:
#         fieldnames = ['Date', 'Time', 'Temperature', 'Humidity']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writerow({'Date': datetime.date.today(), 'Time': datetime.datetime.now().time(), 'Temperature': temp, 'Humidity': hum})

# while True:
#     try:
#         temp, hum = random(25,40), random(30,40)
#         if temp is not None and hum is not None:
#             print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, hum))
#             #write_csv(temp, hum)
#             time.sleep(3)
#         else:
#             print('Failed to get reading. Try again!')
#             time.sleep(3)
#     except KeyboardInterrupt:
#         print("Keyboard Interrupt")
#         break
#     except:
#         print("Error")
#         break

if __name__ == "__main__":
    app.run(debug=True)