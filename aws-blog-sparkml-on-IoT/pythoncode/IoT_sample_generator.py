from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from datetime import datetime
import sys
import time
import random

# Read in command-line parameters
#Please change host below to your host. please remember to use correct region.
host = "XXX.iot.us-east-1.amazonaws.com"

#make sure certificate names matches with actual certificates and path
rootCAPath = "./certs/airsensor-root.pem"
certificatePath = "./certs/airsensor-certificate.pem.crt"
privateKeyPath = "./certs/airsensor-private.pem.key"
topicname= ""
#the location data set contains sensor id, logitude and latitude. This data set will be randomized while publishing data
locationdataset =("111,37.733795,-122.446747","112,41.881832,-87.62317","113,32.89748,-97.040443","114,29.424349,-98.491142","115,25.761681,-80.191788","116,33.753746,-84.38633","117,35.227085,-80.843124","118,40.73061,-73.935242","119,39.941738,-82.992172","120,38.580917,-90.244598","121,44.986656,-93.258133","122,43.618881,-116.215019","123,36.114647,-115.172813","124,36.174465,-86.76796","125,38.889931,-77.009003","126,41.76371,-72.68509","127,43.053619,-89.377808","128,38.931774,-94.579025","129,39.103119,-84.512016","130,34.746483,-92.289597","131,35.787743,-78.644257","132,35.002865,-89.997658","133,43.092461,-79.04715","134,40.806862,-96.681679","135,41.619549,-93.598022","136,42.361145,-71.057083","137,47.608013,-122.335167","138,39.742043,-104.991531","139,40.758701,-111.876183")

#this is data set for sensor data. there are many 100's in the set as 100 is normal air reading and most likely air will be normal more often.
sensordataset=[100, 100, 100, 100, 100, 100, 100,100, 100, 100, 100, 210, 310, 410, 510, 610, 660, 650, 660, 670, 700, 710, 780]

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
    locationdata = random.choice(locationdataset)
    sensordata  = random.choice(sensordataset)
    datetimenow = str(datetime.now())
    message = '{0},{1},{2} \n'.format(locationdata,sensordata,datetimenow)
    print (message)
    time.sleep(1)
    myAWSIoTMQTTClient.publish(topicname, message, 1)
