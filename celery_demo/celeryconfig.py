# /bin/python3


BROKER_URL='redis://192.168.48.2:6379/1'

CELERY_RESULT_BACKEND='redis://192.168.48.2:6379/2'

CELERY_TIMEZONE='Asia/Shanghai'#不指定时区的话默认采用UTC

#导入指定的任务模块
CELERY_IMPORTS=(
    'celerywithconfig.task1',
)
