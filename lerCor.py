from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
sensorLinhaA = ColorSensor(Port.B)
sensorLinhaB = ColorSensor(Port.F)
preto = []

def verPreto(sensor):
    if preto[0] < sensor.hsv().h < preto[1] and preto[2] < sensor.hsv().s < preto[3] and preto[4] < sensor.hsv().v < preto[5]:
        return True
    else:
        return False

def calibrar(lista):
    watch = StopWatch()
    dic = {"h":[], "s": [], "v": []}
    while 100 > watch.time():
        dic["h"].append(sensorLinhaA.hsv().h)
        dic["s"].append(sensorLinhaA.hsv().s)
        dic["v"].append(sensorLinhaA.hsv().v)

        dic["h"].append(sensorLinhaB.hsv().h)
        dic["s"].append(sensorLinhaB.hsv().s)
        dic["v"].append(sensorLinhaB.hsv().v)
    lista.append(min(dic["h"]) - 5) 
    lista.append(max(dic["h"]) + 5) 
    lista.append(min(dic["s"]) - 5) 
    lista.append(max(dic["s"]) + 5) 
    lista.append(min(dic["v"]) - 5) 
    lista.append(max(dic["v"]) + 5)
    return

calibrar(preto)
print(preto)


  
    


 


