from boto import kinesis
from datetime import datetime
import time
import sys
#import testdata
import random
import json
kinesis = kinesis.connect_to_region("us-west-2")

# Phoenix #
latitudedataset= ("37.733795","41.881832","32.89748","29.424349","25.761681","33.753746","35.227085","40.73061","39.941738","38.580917","44.986656","43.618881","36.114647","36.174465","38.889931","41.76371","43.053619","38.931774","39.103119","34.746483","35.787743","35.002865","43.092461","40.806862","41.619549","42.361145","47.608013","39.742043","40.758701","33.572162")
longitudedataset= ("-122.446747","-87.62317","-97.040443","-98.491142","-80.191788","-84.38633","-80.843124","-73.935242","-82.992172","-90.244598","-93.258133","-116.215019","-115.172813","-86.76796","-77.009003","-72.68509","-89.377808","-94.579025","-84.512016","-92.289597","-78.644257","-89.997658","-79.04715","-96.681679","-93.598022","-71.057083","-122.335167","-104.991531","-111.876183")

#the location data set contains sensor id, logitude and latitude. This data set will be randomized while publishing data
#locationdataset =("111,37.733795,-122.446747","112,41.881832,-87.62317","113,32.89748,-97.040443","114,29.424349,-98.491142","115,25.761681,-80.191788","116,33.753746,-84.38633","117,35.227085,-80.843124","118,40.73061,-73.935242","119,39.941738,-82.992172","120,38.580917,-90.244598","121,44.986656,-93.258133","122,43.618881,-116.215019","123,36.114647,-115.172813","124,36.174465,-86.76796","125,38.889931,-77.009003","126,41.76371,-72.68509","127,43.053619,-89.377808","128,38.931774,-94.579025","129,39.103119,-84.512016","130,34.746483,-92.289597","131,35.787743,-78.644257","132,35.002865,-89.997658","133,43.092461,-79.04715","134,40.806862,-96.681679","135,41.619549,-93.598022","136,42.361145,-71.057083","137,47.608013,-122.335167","138,39.742043,-104.991531","139,40.758701,-111.876183")

sensorsids=[0,1,2,3,4,5,6,7,8,9]
patitionKey = random.choice('abcdefghij')
sensordataset=[100, 150, 200, 340, 560, 690, 450, 210, 310, 410, 510, 610, 710]
for i in xrange(100):
    sensordata = random.choice(sensordataset)
    sensorid= random.choice(sensorsids)
    latitude = random.choice(latitudedataset)
    longitude= random.choice(longitudedataset)
    datetimenow = str(datetime.now())
    timenow = datetimenow.split()[1]
    seconds = timenow.split(':')[2]

    #message = '{0},{1},{2},{3},{4}'.format(sensorid,latitude,longitude,sensordata,datetimenow)
    #messsage = json.dumps(message)
    message = str(sensorid)+','+str(latitude)+','+str(longitude)+','+str(sensordata)+','+str(seconds)
    print (message)
    kinesis.put_record(str(sys.argv[1]), message, patitionKey)