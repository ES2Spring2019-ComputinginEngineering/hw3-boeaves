#Name: Bo Eaves
#Partner: Mo Liu
#I worked on this assignmeng with Mo with assistance from Olivia and Brian

import microbit
import math #importing the libraries

def measuring_tilt_in_3D(a, b, c):
    return math.atan2(a, math.sqrt(b**2+c**2))

while True:
    microbit.sleep(100)
    (x, y, z) = microbit.accelerometer.get_values() #this function doesn't take any parameter
    Ax = math.degrees(measuring_tilt_in_3D(x, y, z))
    Ay = math.degrees(measuring_tilt_in_3D(y, x, z))
    print("x = ", (Ax))
    print("y = ", (Ay))
    if Ax < -10:
        if Ay < -10:
            microbit.display.show(microbit.Image.ARROW_NW)
        elif Ay > 10:
            microbit.display.show(microbit.Image.ARROW_SW)
        else:
            microbit.display.show(microbit.Image.ARROW_W)
    elif Ax > 10:
        if Ay < -10:
            microbit.display.show(microbit.Image.ARROW_NE)
        elif Ay > 10:
            microbit.display.show(microbit.Image.ARROW_SE)
        else:
            microbit.display.show(microbit.Image.ARROW_E)
    else:
        if Ay < -10 and (Ax < 10 and Ax > -10):
            microbit.display.show(microbit.Image.ARROW_N)
        elif Ay > 10 and (Ax < 10 and Ax > -10):
            microbit.display.show(microbit.Image.ARROW_S)
        else:
            microbit.display.show(microbit.Image.HAPPY)