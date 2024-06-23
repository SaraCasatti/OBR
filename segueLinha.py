from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
sensorLinhaA = ColorSensor(Port.B)
sensorLinhaB = ColorSensor(Port.F)
frente = UltrasonicSensor(Port.D)
sensorLinhaC = ColorSensor(Port.C)

right_motor = Motor(Port.A)
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=32, axle_track=145)
forca = 50
kp = 2.5
verde = [175, 196, 44, 60, 17, 29]
cinza = [193, 215, 10, 22, 62, 77]
preto = [175, 215, 2, 20, 12, 22]
vermelho =[347, 359, 82, 93, 55, 69]
branco = [163, 203, -2, 12, 82, 98]

def verBranco(sensor):
    if branco[0] < sensor.hsv().h < branco[1] and branco[2] < sensor.hsv().s < branco[3] and branco[4] < sensor.hsv().v < branco[5]:
        return True
    else:
        return False

def verVermelho(sensor):
    if vermelho[0] < sensor.hsv().h < vermelho[1] and vermelho[2] < sensor.hsv().s < vermelho[3] and vermelho[4] < sensor.hsv().v < vermelho[5]:
        return True
    else:
        return False


def verCinza(sensor):
    if cinza[0] < sensor.hsv().h < cinza[1] and cinza[2] < sensor.hsv().s < cinza[3] and cinza[4] < sensor.hsv().v < cinza[5]:
        return True
    else:
        return False

def verPreto(sensor):
    if preto[0] < sensor.hsv().h < preto[1] and preto[2] < sensor.hsv().s < preto[3] and preto[4] < sensor.hsv().v < preto[5]:
        print("preto")
        return True
    else:
        return False


def cima():
    robot.straight(-800)
    robot.turn(-93)
    robot.straight(-400)
    return

def obstaculo():
    def teste(tam):
        cont = 0
        while (cont*5 < tam):
            if verPreto(sensorLinhaA) or verPreto(sensorLinhaB) or verPreto(sensorLinhaC):
                robot.straight(-50)
                robot.turn(-95)
                return True
            cont += 1
            robot.straight(-5)
        return False

    robot.turn(-100)
    robot.straight(-180)

    robot.turn(100)
    if teste(300):
        return

    robot.turn(100)
    if teste(320):
        return

    robot.turn(100)
    if teste(300):
        return



def verVerde(sensor):
    if 180 < sensor.hsv().h < 195 and 40 < sensor.hsv().s < 65 and 10 < sensor.hsv().v < 28:
        return True
    else:
        return False

def verde():
    robot.turn(5)
    direita = False
    esquerda = False
    watch = StopWatch()
    print(watch.time())
    while 1500 > watch.time():
        if verVerde(sensorLinhaA):
            direita = True
            #left_motor.run_angle(100, 180, wait=True)
        if verVerde(sensorLinhaB):
            esquerda = True

    print("Direita:", direita)
    print("Esquerda:", esquerda)

    if direita and esquerda:
        print("dois")
        robot.turn(190, wait=True)
    elif direita:
        print("direita")
        robot.straight(-50)
        robot.turn(-95, wait=True)
    elif esquerda:
        print("esquerda")
        robot.straight(-50)
        robot.turn(95, wait=True)
    else:
        robot.straight(15)
        w = StopWatch()
        f = False
        while 1000 > w.time():
            if verPreto(sensorLinhaC):
                f = True
        if f:
            robot.straight(-40)
            return
        else:
            robot.turn(10)
            robot.straight(-15)
            verde()
            return
    return

while True:
    if verVerde(sensorLinhaA) or verVerde(sensorLinhaB) or verVerde(sensorLinhaC):
        robot.stop()
        print("verde")
        verde()
    elif frente.distance() < 60:
        print("obstaculo")
        obstaculo()
    elif verCinza(sensorLinhaA) and verCinza(sensorLinhaB):
        print("cima")
        cima()
    elif verVermelho(sensorLinhaA) and verVermelho(sensorLinhaB):
        robot.stop()
    else:
        if verBranco(sensorLinhaC) and verBranco(sensorLinhaA) and verBranco(sensorLinhaB):
            robot.straight(-10)
        erro = sensorLinhaA.reflection() - sensorLinhaB.reflection()
        correcao = kp * erro
        right_motor.dc(-(forca + correcao))
        left_motor.dc(-(forca - correcao))