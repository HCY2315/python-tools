# /bin/python3

import time

#从__init__.py中导入实例化的Celery myapp
from celerywithconfig import myapp

@myapp.task
def add(x,y):
    print("aaaaa", x+y)
    time.sleep(3)
    print("bbbbb", x+y)
    return x+y