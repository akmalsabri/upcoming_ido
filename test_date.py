import time
from datetime import datetime, timedelta



# initializing datelist
test_date_list = [datetime(2020, 4, 8), datetime(2016, 8, 18), 
                  datetime(2018, 9, 24), datetime(2019, 6, 10),
                  datetime(2021, 8, 10)]
               
# printing original list
print("The original list is : " + str(test_date_list))
  
# initializing test date 
test_date = datetime.now()
print(test_date)
  
# shorthand using lambda function for compact solution
res = min(test_date_list, key=lambda sub: abs(sub - test_date))
  
# printing result
print("Nearest date from list : " + str(res))