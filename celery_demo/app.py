# /bin/python3
import sys 
sys.path.append("../")

from celerywithconfig import task1


task1.add.delay(2, 4)
print ('end...')