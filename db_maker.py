import pymysql

db = pymysql.connect(host="localhost", user="root")
cursor = db.cursor()

cursor.execute("CREATE DATABASE login_database")
db.commit()
cursor.close()
db.close()

db = pymysql.connect(host="localhost", user="root", database="login_database")
cursor = db.cursor()
cursor.execute("CREATE TABLE testing (id int(11) AUTO_INCREMENT,"
               "username varchar(150) NOT NULL,"
               "password varchar(30) NOT NULL,"
               "PRIMARY KEY (id))")
db.commit()
cursor.close()
db.close()
