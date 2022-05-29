from bottle import run , route, template, static_file , get , post , response , view , request
import os 
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
collection = mydb["ido_solanium"]

# set directory

my_dir = os.getcwd()



@route('/static/<filepath:path>')
def serve_static_content(filepath):
    my_root = os.path.join(my_dir,'static')

    return static_file(filepath, root= my_root)






@route('/')
def serve_homepage():
    return template('./static/index.html')

@route("/home", method='GET')
def test ():

    master_client = MongoClient("mongodb://{}:{}@{}:{}".format(user,pwd,ip,port))
    mydb = master_client["crepetoast"]
    collection = mydb["ido_solanium"]

    coll_sol = collection.find()
    #print(coll_sol)

    list_dict = []

    for i in coll_sol:
        #print(i)

        # for i in ix:

        #     print(i)


        data_ = {

            'IDO_Name'                      : i['IDO_Name'],
            'IDO_Symbol'                    : i['IDO_Symbol'],                
            'IDO_Logo'                      : i['IDO_Logo'],
            'IDO_website'                   : i['IDO_website'],
            'IDO_subtitle'                  : i['IDO_subtitle'],
            'IDO_description'               : i['IDO_description'],
            'Whitelist_start'               : i['Whitelist_start'],  
            'Whitelist_start_str'           : i['Whitelist_start_str'],
            'Sale_start'                    : i['Sale_start'], 
            'Sale_start_str'                : i['Sale_start_str'],             
            'Upcoming_Distribution'         : i['Upcoming_Distribution'],
            'Upcoming_Distribution_str'     : i['Upcoming_Distribution_str'],
            'Distribution_Status'           : i['Distribution_Status'],
            'Website'                       : i['Coin']
    
        }

        list_dict.append(data_)
 

    return template('./static/index.html', data= list_dict)

@route("/home_", method='GET')
def test ():

    master_client = MongoClient("mongodb://{}:{}@{}:{}".format(user,pwd,ip,port))
    mydb = master_client["crepetoast"]
    
    # solanium collection
    coll_sol = mydb["ido_solanium"]

    coll_sol_find = coll_sol.find()
    print(coll_sol_find)

    # collection avalaunch
    coll_xava = mydb["ido_avalaunch"]

    coll_xava_find = coll_xava.find()
    print(coll_xava_find)

    list_dict = []

    for i in coll_sol_find:
        #print(i)

        # for i in ix:

        #     print(i)


        data_ = {

            'IDO_Name'                      : i['IDO_Name'],
            'IDO_Symbol'                    : i['IDO_Symbol'],                
            'IDO_Logo'                      : i['IDO_Logo'],
            'IDO_website'                   : i['IDO_website'],
            'IDO_price'                     : i['IDO_price_usd'],
            'IDO_subtitle'                  : i['IDO_subtitle'],
            'IDO_description'               : i['IDO_description'],
            'Whitelist_start'               : i['Whitelist_start'], 
            'Whitelist_start_str'           : i['Whitelist_start_str'], 
            'Sale_start'                    : i['Sale_start'],              
            'Sale_start_str'                : i['Sale_start_str'],             
            'Upcoming_Distribution'         : i['Upcoming_Distribution'],
            'Upcoming_Distribution_str'     : i['Upcoming_Distribution_str'],
            'Distribution_Status'           : i['Distribution_Status'],
            'Website'                       : i['Coin']
    
        }

        list_dict.append(data_)

    list_dict_xava =[] 


    for i in coll_xava_find:
        #print(i)

        # for i in ix:

        #     print(i)


        data_ = {

            'IDO_Name_'                      : i['IDO_name'],
            'IDO_Symbol_'                    : i['IDO_symbol'],                
            'IDO_Logo_'                      : i['IDO_Logo'],
            'IDO_price'                      : i['IDO_price_usd'],
            'IDO_website_'                   : i['IDO_website'],
            'IDO_description_'               : i['IDO_description'],
            'Whitelist_start_'               : i['Whitelist_start'],  
            'Sale_start_'                    : i['Stacking_round'],              
            'Upcoming_Distribution_'         : i['Allocate']
    
        }

        list_dict_xava.append(data_)

    




    
 

    return template('./static/index_1.html', data= list_dict , data2= list_dict_xava)






    


if __name__ == "__main__":
    run(host='localhost', port=8080 , debug=True)
