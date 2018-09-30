import time

from moisture_sensor import *

while True:
    time.sleep(5)
    value = MoistureRead()
    if value:
        print "I am drowning!"
    else:
        print "I am safe.. phew"
   
