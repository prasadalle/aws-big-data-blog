from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from datetime import datetime
import sys
import time
import random
import urllib2


#Please change host below to your host. please remember to use correct region.
host = "xxxx.iot.us-east-1.amazonaws.com" 

#make sure certificate names matches with actual certificates and path
rootCAPath = "./certs/airsensor-root.pem"
certificatePath = "./certs/airsensor-certificate.pem.crt"
privateKeyPath = "./certs/airsensor-private.pem.key"
topicname= ""

#make Change URL to actual Arduino URL
#change following IP Address to arduino yun's IP address
url = 'http://192.168.1.136/arduino/analog/0'
# sensor id, lattitude, longitude rocordset


myAWSIoTMQTTClient = AWSIoTMQTTClient(topicname)
myAWSIoTMQTTClient.configureEndpoint(host, 8883)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()

# Publish to the same topic in a loop foreverloopCount = 0
while True:
    topicname = "iotairqualitydata-" + str(datetime.now().strftime("/%Y/%m/%d/%H"))
    # location data longitute and lattitude is hardcoded, you can change it to any other location
    locationdata = "33.572162,-112.087966"
    f = urllib2.urlopen(url)
    RESTdata  = f.read()
    RESTdata  = RESTdata.strip()
    sensordata = RESTdata[-3:]
    datetimenow = str(datetime.now())
    message = '{0},{1},{2} \n'.format(locationdata,sensordata,datetimenow)
    print (message)
    time.sleep(1)
    myAWSIoTMQTTClient.publish(topicname, message, 1)