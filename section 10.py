### expetion handler
# specific error in first 
# run genral when no specific handlig

try :
    x=1
    y=0
    print (x/y)
except ZeroDivisionError:
    print (" we can't divide on zero ")
except :
    print (" this is genral hundler ")

raise Exception ("ahmed")

import calc ### first way to import 
calc.sum(1,2)

from calc import * ### second way to import 
subtract(1,1)

import time
import datetime

a = time.time()
datetime.date.fromtimestamp(a) # converts seconds to day