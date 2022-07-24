#Code for Sending sms when temperature fluctuates
import configm                  # config file
from boltiot import Sms, Bolt   # importing Bolt from boltiot module
import json, time               # library for handling JSON data
                                # module for sleep operation

minimum_limit = 205 #20 deg celcius
maximum_limit = 307 #30 deg celcius


mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)


while True: 
    #getting the sensor value from the iot device
    print ("Reading sensor value")
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    print("Sensor value is: " + str(data['value']))
    
    try: 
        #Checking if the sensor value exceeds the threshold
        sensor_value = int(data['value']) 
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("The Current temperature sensor value is " +str(sensor_value*0.09765)+ " degree celcius")
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
        
    #wait for 10 seconds
    time.sleep(10)