import pymongo
from pymongo import mongo_client

from pymongo import MongoClient
import credentials

# Access mongodb
user = credentials.login['username_db']
pwd = credentials.login['password_db']
ip = credentials.login['ip_db']
port = credentials.login['port_db']


# Accessing mongodb cluster 
master_client = MongoClient("mongodb://{}:{}@{}:{}".format(user,pwd,ip,port))


# Save to database

mydb = master_client["crepetoast"]
collection = mydb["ido_solanium"]

coll_sol = collection.find()


for ix in coll_sol:

    print(ix)