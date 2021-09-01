#/bin/python3
# from celery import Celery
# celery_app = Celery('testdemo') # 实例化celery对象
# celery_app.config_from_object('demo.celery_config') # 配置文件加载
from celery import Celery

myapp=Celery('demo')

#通过Celery实例加载配置模块celeryconfig.py
myapp.config_from_object('celerywithconfig.celeryconfig')
