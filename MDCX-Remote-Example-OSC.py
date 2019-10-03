#!/usr/bin/env python3
# Sample for remote control the MDC-X system
#
# This example uses the MDC-OSC interface.
# For more information please see the "Remote Control" section in the MDC-X manual.
#

# Copyright (c) 2017 by Dynamic Projeciton Institute GmbH, Vienna, Austria
# Author: Martin Willner <willner@dynamicprojection.com>

from OSC import OSCClient, OSCMessage
import socket
import time

# CHANGE THIS TO THE MDC-X Server IP - make sure the OSC and MDC Proxy is enabled! 
MDCX_HOST="182.168.0.211" #This is the DEFAULT MDC-X IP on the LAN Port
#MDCX_HOST="192.168.0.162"

#####################################
MDCX_OSC_PORT=7475

# wrappers for SYS and OSC
def oscsender(obj,topic,msg):
	try:
		if msg is None:
			obj.send(OSCMessage(topic))
			print ("OSC LOG: TOPIC("+str(topic)+")")
		else:
			obj.send(OSCMessage(topic,msg))
			print ("OSC LOG: TOPIC("+str(topic)+") MSG("+str(msg)+")")
	except:
		print ("OSC ERROR - failed to send!")




# OSC socket for MDC Show control
mdcx_osc = OSCClient()
mdcx_osc.connect((MDCX_HOST, MDCX_OSC_PORT))

########################################################
# EXAMPLES ARE HERE 
########################################################



# OSC Project Control
'''
Supported commands are:
/mdc_layer$X_preset$P : Load Presets $P on layer $X
/mdc_layer$X_preset_next : Select next preset
/mdc_layer$X_preset_previous : Select previous preset
/mdc_layer$X_media$Y : Load Media $Y on layer $X
/mdc_layer$X_map$M: Select Map $M on layer $X. If $M is set to 0 then ALL maps are selected.
/mdc_layer$X_map_all : Same as /mdc_layer$X_map0
/mdc_layer$X_mm_$M_$Y : Same as /mdc_layer$X_map$M + sleep 1 sec + /mdc_layer$X_media$Y
/mdc_timeline_play : Set playback to play
/mdc_timeline_pause : Set playback to pause
/mdc_timeline_stop : Set playback to stop
/mdc_killanimation : Kill all animation keyframes
/mdc_restart : Restart project
/mdc_fullscreen : Toggle fullscreen mode
/mdc_playlist$Z : Select playlist item $Z
/mdc_playlist_next : Select next playlist item
/mdc_playlist_previous : Select previous playlist item
/mdc_glm_on : Global Lock Media ON 
/mdc_glm_off : Global Lock Media OFF
'''
while True:
	oscsender(mdcx_osc,"/mdc_layer1_preset1",1.0)
	time.sleep(3)
	oscsender(mdcx_osc,"/mdc_layer1_preset2",1.0)	
	time.sleep(3)
	oscsender(mdcx_osc,"/mdc_layer1_map_all",1.0)
	time.sleep(3)
	oscsender(mdcx_osc,"/mdc_layer1_media1",1.0)	
	time.sleep(3)
	oscsender(mdcx_osc,"/mdc_layer1_media2",1.0)	
	time.sleep(3)
	oscsender(mdcx_osc,"/mdc_layer1_media3",1.0)
	time.sleep(3)
	oscsender(mdcx_osc,"/mdc_timeline_pause",1.0)	
	time.sleep(3)
	oscsender(mdcx_osc,"/mdc_timeline_play",1.0)
	time.sleep(1)
	

