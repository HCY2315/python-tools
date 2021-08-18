# /bin/python3

# 写入开头
filewrite = open("./docker-compose.yaml", "a")
value = '''version: '2'
services:
'''
filewrite.close
filewrite.write(value)

i = 151
while i < 201:
    fileread = open("./temp", "r", encoding="utf-8")
    filewrite = open("./docker-compose.yaml", "a")
    fileread.seek(0)

    # 替换模版中的数据
    for (num,value) in enumerate(fileread):
        if "aaa" in value:
            value = value.replace("aaa:", "c{0}:".format(i))
        if "bbb" in value:
             value = value.replace("bbb", "{0}".format(i))
        filewrite.write(value)
        
    fileread.close()
    filewrite.close()
    i += 1

# 写入结尾
filewrite = open("./docker-compose.yaml", "a")
value = '''
networks:
    mynet1:
        ipam:
            config:
            - subnet: 172.30.0.0/16
'''
filewrite.write(value)
filewrite.close