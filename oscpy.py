#!/usr/bin/env python3
from OSC import OSCClient, OSCMessage
import socket
import time
import math

MDCX_HOST="localhost"
MDCX_OSC_PORT=7475 

mdcx_osc = OSCClient()
mdcx_osc.connect((MDCX_HOST, MDCX_OSC_PORT))

def oscsender(obj,topic,msg):
	try:
		obj.send(OSCMessage(topic,msg),0.1)
		print ("OSC MESSAGE: TOPIC("+str(topic)+") MSG("+str(msg)+")")
	except:
		print ("OSC ERROR - failed to send!")
	print ("\n")



i=0.0
while True:
	print ("***** /mdc_layer1_preset Animation *****")
	for i in range(1,3):
		print ("--> Calling PRESET "+str(i))
		oscsender(mdcx_osc,"/mdc_layer1_preset"+str(i),(1))
		time.sleep(3)

	print ("***** /mdc_layer1_media Animation *****")
	for i in range(1,3):
		print ("--> Calling MEDIA "+str(i))
		oscsender(mdcx_osc,"/mdc_layer1_media"+str(i),(1))
		time.sleep(3)

	print ("***** /mdc_dmx  Animation *****")
	print ("--> Set DMX: #1:0 #2:0 #3:0 #4:0")
	oscsender(mdcx_osc,"/mdc_dmx",(1,1,0,2,0,3,0,4,0))
	time.sleep(3)
	print ("--> Set DMX: #1:255 #2:255 #3:255 #4:255")
	oscsender(mdcx_osc,"/mdc_dmx",(1,1,255,2,255,3,255,4,255))
	time.sleep(3)
	print ("--> Set DMX: #1:128 #2:0 #3:128 #4:0")
	oscsender(mdcx_osc,"/mdc_dmx",(1,1,128,2,0,3,128,4,0))
	time.sleep(3)
	i=0.0
	while i < 30:
		oscsender(mdcx_osc,"/mdc_dmx",(1,1,int(128-math.sin(i)*10.0),2,0,3,int(128-math.sin(i)*10.0),4,0))
		i=i+0.05
		time.sleep(0.01)
	time.sleep(1)
	print ("Set DMX: #1:128 #2:0 #3:128 #4:0")
	oscsender(mdcx_osc,"/mdc_dmx",(1,1,128,2,0,3,128,4,0))
	time.sleep(3)



	i=0.0
	print ("***** /mdc_map Animation *****")
	while i < 20:
		oscsender(mdcx_osc,"/mdc_map",(1,1,0.0,0.0,math.sin(i),0.0,1.0,math.cos(i),0.0,1.0))
		i=i+0.05
		time.sleep(0.01)
	print ("Set /mdc_map 1 1 0.0 0.0 1.0 0.0 1.0 1.0 0.0 1.0")
	oscsender(mdcx_osc,"/mdc_map",(1,1,0.0,0.0,1.0,0.0,1.0,1.0,0.0,1.0))
	time.sleep(3)

	i=0.0
	print ("***** /mdc_tex Animation *****")
	while i < 10:
		oscsender(mdcx_osc,"/mdc_tex",(1,1,0.0,0.0,math.sin(i)+1,0.0,math.sin(i)+1,math.sin(i)+1,0.0,math.sin(i)+1))
		i=i+0.05
		time.sleep(0.01)
	print ("Set /mdc_tex 1 1 0.0 0.0 1.0 0.0 1.0 1.0 0.0 1.0")
	oscsender(mdcx_osc,"/mdc_tex",(1,1,0.0,0.0,1.0,0.0,1.0,1.0,0.0,1.0))
	time.sleep(3)

	print ("***** /mdc_maploadmedia Animation *****")
	oscsender(mdcx_osc,"/mdc_maploadmedia",(1,1,1))
	time.sleep(0.1)
	oscsender(mdcx_osc,"/mdc_maploadmedia",(1,2,1))
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_maploadmedia",(1,1,2))
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_maploadmedia",(1,2,3))
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_maploadmedia",(1,1,1))
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_maploadmedia",(1,2,1))
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_p",(1,1))
	time.sleep(2)
	oscsender(mdcx_osc,"/mdc_p",(1,2))
	time.sleep(2)
	oscsender(mdcx_osc,"/mdc_p",(1,3))
	time.sleep(2)



	oscsender(mdcx_osc,"/mdc_dynamicpreset",(1,1,1.0,1.0,1.0,1.0))
	time.sleep(3)
	oscsender(mdcx_osc,"/mdc_dynamicpreset",(1,2,2.0,2.0,1.0,1.0))
	time.sleep(3)
	oscsender(mdcx_osc,"/mdc_dynamicpreset",(1,3,3.0,3.0,1.0,1.0))
	time.sleep(3)


#	oscsender(mdcx_osc,"/mdc_load",(1.0))	
#	time.sleep(2)
	print ("***** /mdc_artnet ON/OFF *****")
	oscsender(mdcx_osc,"/mdc_artnet",(1.0))
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_artnet",(0))
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_artnet",(1.0))
	time.sleep(1)

	
	while i < 3.141:
		oscsender(mdcx_osc,"/mdc_map",(1,1,0.0,0.0,math.sin(i),0.0,1.0,1.0,0.0,1.0))
		i=i+0.01
		time.sleep(0.01)
	oscsender(mdcx_osc,"/mdc_map",(1,1,0.0,0.0,1.0,0.0,1.0,1.0,0.0,1.0))
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_map",(1,1,0.25,0.25,.75,0.25,.75,.75,.25,.75))
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_tex",(1,1,0.25,0.25,.75,0.25,.75,.75,.25,.75))
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_tex",(1,1,0.0,0.0,1.0,0.0,1.0,1.0,0.0,1.0))
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_map",(1,1,0.0,0.0,1.0,0.0,1.0,1.0,0.0,1.0))
	time.sleep(1)
	
	oscsender(mdcx_osc,"/mdc_int_int",(1,2))
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_int_float",(1,1.0))	
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_int_str",(1,"abcd"))	
	time.sleep(1)
	oscsender(mdcx_osc,"/mdc_float_str",(3.0,"abcd"))	
	time.sleep(1)
	

