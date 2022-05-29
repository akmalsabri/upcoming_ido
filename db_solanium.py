# ada is_closed , true , false
# https://www.solanium.io/

#from pymongo import collection
from pymongo import MongoClient
import requests
import time 
from datetime import datetime, timedelta
from datetime import datetime 
import sys
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

# Save to database
# myclient = MongoClient("mongodb://localhost:27017/")
# mydb = myclient["IDO_upcoming_03"]
# collection = mydb["collection_solanium"]

def funcfindnearest(list_date, base_date):

    b_d = datetime.strptime(base_date, "%m/%d %I:%M %p")
    def func(x):
       d =  datetime.strptime(x[0], "%m/%d %I:%M %p")
       delta =  d - b_d if d > b_d else timedelta.max
       return delta
    return min(list_date, key = func)



def solanium_ido():

    url_ = 'https://api.solanium.com/solana/projects/?format=json'

    r = requests.get(url_)

    time.sleep(2)

    data_ = r.json()

    list_url = []


    for i in data_:

        bb = i['is_closed']

        if bb == False:


            #####################################################################
            # IDO id
            ido_id   = i['id']

            #####################################################################
            # IDO Name
            ido_name = i['name']
            
            ######################################################################
            # IDO Symbol
            sale_token_ = i['sale_token']
            ido_symbol  = sale_token_['ticker']

            ####################################################################
            # IDO price
            #price = i['deposit_token']

            ido_price = i['token_price']




            ####################################################################    
            # url IDO

            list_url.append(i['url'])

            ido_url = f"https://www.solanium.io/project/{i['url']}"

            ######################################################################
            # IDO Logo
            ido_logo = sale_token_['logo']

            #######################################################################
            # Website

            ido_website = i['website']

            #######################################################################
            # Subtitle

            ido_subtitle = i['sub_title']

            #######################################################################
            # Description

            ido_description = i['description']

            #######################################################################
            # Social network
            # twitter
            twitter_link = 'https://twitter.com/'+i['twitter_username']

            # Discord channel
            discord_channel = i['discord']



            #######################################################################
            # Whitelist 
            # Start
            # Convert start str to datetime
            wh_start = i['whitelist_start']  

            

            if wh_start is None:

                wh_start_dt = 'TBA'
                wh_end_dt = 'TBA'
                wh_start_str ='TBA'
                wh_end_str ='TBA'

            else:

                # convert to datetime
                wh_start_dt = datetime.strptime(wh_start, '%Y-%m-%dT%H:%M:%SZ')
                wh_start_str = wh_start_dt.strftime('%d-%b-%Y %H:%M')+' UTC'

                # End
                wh_end = i['whitelist_end']

                # convert to datetime
                wh_end_dt = datetime.strptime(wh_end, '%Y-%m-%dT%H:%M:%SZ')
                wh_end_str = wh_end_dt.strftime('%d-%b-%Y %H:%M')+' UTC'

            #########################################################################
            # Sale start
            # Start
            # Convert start str to datetime
            sale_start = i['sale_start']  


            if sale_start is None:

                sale_start_dt   = 'TBA'
                sale_end_dt     = 'TBA'
                sale_start_str  = 'TBA'
                sale_end_str    = 'TBA'

            else:

                # convert to datetime
                sale_start_dt = datetime.strptime(sale_start, '%Y-%m-%dT%H:%M:%SZ')
                sale_start_str = sale_start_dt.strftime('%d-%b-%Y %H:%M')+' UTC'

                # End
                sale_end = i['sale_end']  

                # convert to datetime
                sale_end_dt = datetime.strptime(sale_end, '%Y-%m-%dT%H:%M:%SZ')
                sale_end_str = sale_end_dt.strftime('%d-%b-%Y %H:%M')+' UTC'


            #######################################################################
            # Distribution start
            # not in datetime
            distribution_start = i['claim_start']  

            if distribution_start is None:
                
                status_distribution = False

                distribution_start_dt = 'TBA'
                distribution_start_str = 'TBA'

            else:
                status_distribution = True

                distribution_start_dt = datetime.strptime(distribution_start, '%Y-%m-%dT%H:%M:%SZ')
                #distribution_start_str = distribution_start_dt.strftime("%Y-%m-%d %H:%M") 
                distribution_start_str = distribution_start_dt.strftime('%d-%b-%Y %H:%M')+' UTC'

            ###############################################################################
            # compare date

            list_date = [wh_start_dt,wh_end_dt,sale_start_dt,sale_end_dt,distribution_start_dt]

            if status_distribution == False :

                nearest_date = None

            else:

                today_date = datetime.now()

                res = min(list_date, key=lambda sub: abs(sub - today_date))

                print('----Nearest---')
                print(res)

                if res == wh_start_dt:

                    if today_date > res :

                        status_date = 'Whitelist Soon'

                    if today_date < res :

                        status_date = 'Whitelisted'

                if res == wh_end_dt:

                    if today_date > res :

                        status_date = 'Whitelist End Soon'

                    if today_date < res :

                        status_date = 'Whitelist End'

                if res == sale_start_dt:

                    if today_date > res :

                        status_date = 'Sale Start Soon'

                    if today_date < res :

                        status_date = 'Sale Start'

                if res == sale_end_dt:

                    if today_date > res :

                        status_date = 'Sale End Soon'

                    if today_date < res :

                        status_date = 'Sale End'            

                if res == distribution_start_dt:

                    if today_date > res :

                        status_date = 'Distribution Coming Soon'

                    if today_date < res :

                        status_date = 'Distributed'                     



            data_ = {

                'No_id'                         : ido_id,
                'IDO_Name'                      : ido_name,
                'IDO_Symbol'                    : ido_symbol,                
                'IDO_Logo'                      : ido_logo,
                'IDO_price_usd'                 : ido_price,
                'IDO_url'                       : ido_url,
                'IDO_website'                   : ido_website,
                'IDO_subtitle'                  : ido_subtitle,
                'IDO_description'               : ido_description,
                'Whitelist_start'               : wh_start_dt, 
                'Whitelist_start_str'           : wh_start_str, 
                'Whitelist_end'                 : wh_end_dt,
                'Whitelist_end_str'             : wh_end_str,
                'Sale_start'                    : sale_start_dt, 
                'Sale_start_str'                : sale_start_str,              
                'Sale_end'                      : sale_end_dt,
                'Sale_end_str'                  : sale_end_str,
                'Upcoming_Distribution'         : distribution_start_dt,
                'Upcoming_Distribution_str'     : distribution_start_str,
                'Distribution_Status'           : status_distribution,
                'Twitter_username'              : twitter_link,
                'Discord_channel'               : discord_channel,
                'Coin'                          : 'Solanium'
      
            }

            print(data_)

            print('-------------------------------')

            #collection.insert_one(data_)

            

if __name__ == "__main__":
    solanium_ido()