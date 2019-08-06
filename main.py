import time

from moisture_sensor import *
from mail import *

counter = 0
while True:
    time.sleep(5)
    value = MoistureRead()
    if value == 0:
        counter = counter + 1
        print "no water detected"
    if counter == 5:
        counter = 0
        sendmail()
