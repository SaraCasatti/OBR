from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
right_motor = Motor(Port.F)
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
sensorV1 = ColorSensor(Port.D)
sensorV2 = ColorSensor(Port.C)

while True:
    right_motor.dc(60)
    left_motor.dc(60)
    c1 = sensorV1.color()
    c2 = sensorV2.color()

    print (c1, c2)


