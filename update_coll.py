# ada is_closed , true , false
# website https://launchpad.avalaunch.app/sales

import requests
import time
from datetime import datetime


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
collection = mydb["ido_avalaunch"]

coll_find = collection.find()

for i in coll_find:

    print(i)

    # newvalues = {"$set":{'Whitelist_start_str':"22-Mar-2022 23:00 UTC",
    # 'Validator_round_str':"28-Mar-2022 14:00 UTC",
    # 'Stacking_round_str':"28-Mar-2022 23:00 UTC",
    # 'Sale_end_str':"29-Mar-2022 14:00 UTC",
    # 'Allocate_str':"01-Apr-2022 22:00 UTC"}}

    # id_dict = i["_id"]
    # print(id_dict)

    # collection.update_one({"_id":id_dict},newvalues)