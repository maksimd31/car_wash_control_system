# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234qwer'

)

# подготовил объект курсора
cursorObject = dataBase.cursor()

# Создаем базу данных.
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
