from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
sensorLinhaA = ColorSensor(Port.A)
sensorLinhaB = ColorSensor(Port.E)
sensorVerdeA = ColorSensor(Port.D)
sensorVerdeB = ColorSensor(Port.C)
right_motor = Motor(Port.F)
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
forca = 70
kp = 2

def verde():
    if sensorVerdeA.color() == Color.GREEN and sensorVerdeB.color() == Color.GREEN:
        robot.turn(850, wait=True)
    elif sensorVerdeA.color() == Color.GREEN:
        print("d")
        #robot.straight(10,wait=True)
        left_mo.run_angle(60, 90, wait=True)
    else:
        print("direita")
        right_motor.run_angle(60, 90, wait=True)


while True: 
    if sensorVerdeA.color() == Color.GREEN or sensorVerdeB.color()== Color.GREEN:
        verde()
    else:
        erro = sensorLinhaA.reflection() - sensorLinhaB.reflection()
        correcao = kp * erro
        right_motor.dc(forca - correcao)
        left_motor.dc(forca + correcao)
    

