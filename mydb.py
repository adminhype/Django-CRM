# Install Myswl on computer
# https://dev.mysql.com/downloads/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python


import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Hq2wqf5gmkto!',
    database="noobco"
)

print("END")