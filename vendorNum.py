#!/usr/bin/env python
#
# Insert a new element in  a MySQLDB1 employee database
# ######################################################


import datetime
import MySQLdb
from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import *


#MySQLDB1
MySQLdb.connect(host="localhost", port=3306, user="MySQLu1", passwd="I123", db="inventory")
try:
    MySQLdb.db_drop('inventory').run()
except:
    pass
MySQLdb.db_create('inventory').run()

tables = ['productName', 'storageLocal', 'brandName', 'prices', 'vendor', 'departments']
for table in tables:
    MySQLdb.db('inventory').table_create(table).run()


#Get contact number from vendor

ContactNum = cursor.execute("""SELECT name, phone_number 
                  FROM vendor 
                  WHERE name=%s 
                  AND clue > %s 
                  LIMIT 5""",
               (name, clue_threshold))

MySQLdb.close()
