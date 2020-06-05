#class Libraries for the bluetooth application

import time

from  bluetooth.ble import BeaconService #<---3rd Party module

service = BeaconService() #<---creating an instance object of the class library

service.start_advertising("11111111-3333-4444-2222-55555555", 1,1,1,200) #<---Advertise the UUID and different ports for spoofing

time.sleep(15)
service.stop_advertise()

print("done.")