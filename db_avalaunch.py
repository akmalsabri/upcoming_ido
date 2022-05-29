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



def get_id_avalaunch():

    url_ = 'https://avalaunch-kyc.herokuapp.com/api/v1/projects'

    r = requests.get(url_)

    time.sleep(2)

    data_ = r.json()

    data_project = data_['projects']

    #print(data_project)
    list_id = []

    for i in data_project:

        id_ = i['id']        
        #print(i['title'])

        state = i['state']
        #print(i['state'])

        if state != 'Ended':

            #print('ada')
            #print(title_)
            list_id.append(id_)
            print(state)

    return list_id

def avalaunch_ido():

    list_id = get_id_avalaunch()

    for i in list_id:

        url_api = 'https://avalaunch-kyc.herokuapp.com/api/v1/projects/{}'.format(i)
        print(url_api)

        r = requests.get(url_api)

        time.sleep(2)

        data_ = r.json()

        #################################################################################3


        #################################################################################
        # Token information

        info_ = data_['project']
        token = info_['token']

        # IDO name
        ido_name = token['name']

        # IDO symbol
        ido_symbol = token['symbol']

        # IDO price in usd
        ido_price = token['token_price_in_usd']

        # IDO url
        ido_url = f"https://avalaunch.app/project-details?id={i}"
        

        ##################################################################################
        # Token logo , description , website


        # IDO logo
        ido_logo = info_['logo_url']

        # IDO description
        ido_description = info_['explanation_text']

        # IDO website
        ido_website = info_['website_url']


        ##################################################################################
        # Timeline date
        timeline = info_['timeline']

        ### Register open

        register_open = int(timeline['registration_opens'])

        # convert to datetime
        register_open_dt = datetime.fromtimestamp(register_open)
        register_open_str = register_open_dt.strftime('%d-%b-%Y %H:%M')+' UTC'


        ## Register close
        register_close = int(timeline['registration_closes'])

        # convert to datetime
        register_close_dt = datetime.fromtimestamp(register_close)
        register_close_str = register_close_dt.strftime('%d-%b-%Y %H:%M')+' UTC'

    
        ### Validator round
        validator_round = int(timeline['validator_round'])

        # convert to datetime
        validator_round_dt = datetime.fromtimestamp(validator_round)
        validator_round_str = validator_round_dt.strftime('%d-%b-%Y %H:%M')+' UTC'

        ### Stacking round
        stacking_round = int(timeline['seed_round'])

        # convert to datetime
        stacking_round_dt = datetime.fromtimestamp(stacking_round)
        stacking_round_str = stacking_round_dt.strftime('%d-%b-%Y %H:%M')+' UTC'

        ### Sale End
        ### Stacking round
        sale_end = int(timeline['sale_ends'])

        # convert to datetime
        sale_end_dt = datetime.fromtimestamp(sale_end)
        sale_end_str = sale_end_dt.strftime('%d-%b-%Y %H:%M')+' UTC'

        ## TGE
        vesting = info_['vesting']
        allocate_round = int(vesting['first_allocation_unlocked_at'])

        # convert to datetime
        allocate_dt = datetime.fromtimestamp(allocate_round)
        allocate_str = allocate_dt.strftime('%d-%b-%Y %H:%M')+' UTC'    

        ###############################################################
        # Social network

        social_net = info_['socials']

        # Twitter
        twitter_link = social_net['twitter']

        # Discord channel
        discord_channel = social_net['discord']


        #print(ido_symbol)

        data_ = {

            "No_id"                         : i,
            'IDO_name'                      : ido_name,
            'IDO_symbol'                    : ido_symbol,
            'IDO_Logo'                      : ido_logo,
            'IDO_url'                       : ido_url,
            "IDO_price_usd"                 : ido_price,
            "IDO_description"               : ido_description,
            "IDO_website"                   : ido_website,
            "Whitelist_start"               : register_open_dt,
            "Whitelist_start_str"           : register_open_str,
            "Whitelist_end"                 : register_close_dt,
            "Whitelist_end_str"             : register_close_str,
            "Validator_round"               : validator_round_dt,
            "Validator_round_str"           : validator_round_str,
            "Stacking_round"                : stacking_round_dt,
            "Stacking_round_str"            : stacking_round_str,
            "Sale_end"                      : sale_end_dt,
            "Sale_end_str"                  : sale_end_str,
            "Allocate"                      : allocate_dt,
            "Allocate_str"                  : allocate_str,
            "Twitter_link"                  : twitter_link,
            'Discord_channel'               : discord_channel,
            'Coin'                          : 'Avalaunch'          
        }  

        print('-----save to database--------')
        print(data_)
        #collection.insert_one(data_)


if __name__ == "__main__":
    avalaunch_ido()       