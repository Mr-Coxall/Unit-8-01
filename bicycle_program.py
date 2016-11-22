# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This main program will create a bicycle object

from bicycle import *

# create an instance of a bicycle
bike1 = Bicycle()
bike2 = Bicycle()

print(bike1.current_state())
bike1.speed_up(10)
print(bike1.current_state())
bike1.apply_brakes(3)
print(bike1.current_state())

print(bike2.current_state())
bike2.speed_up(40)
print(bike2.current_state())
bike2.apply_brakes(12)
print(bike2.current_state())
