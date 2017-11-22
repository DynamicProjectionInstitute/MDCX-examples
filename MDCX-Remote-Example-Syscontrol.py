# Sample for remote control the MDC-X system
#
# This example uses the MDC-Daemon interface.
# For more information please see the "Remote Control" section in the MDC-X manual.
#

# Copyright (c) 2017 by Dynamic Projeciton Institute GmbH, Vienna, Austria
# Author: Martin Willner <willner@dynamicprojection.com>

import socket
import time

# CHANGE THIS TO THE MDC-X Server IP - make sure the OSC and MDC Proxy is enabled!
MDCX_HOST="192.168.0.200" #This is the DEFAULT MDC-X IP on the LAN Port
#MDCX_HOST="192.168.0.162"

#####################################
MDCX_DAEMON_PORT=9999

# wrappers for SYS

def syssender(obj,topic):
	try:
		obj.sendto(topic,(MDCX_HOST,MDCX_DAEMON_PORT))
		print "SYS LOG: TOPIC("+str(topic)+")"
	except:
		print "SYS ERROR - failed to send!"


# UDP socket for the MDCX Daemon connection
mdcx_system = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


########################################################
# EXAMPLES ARE HERE
########################################################

# System Control
'''
commands are:
KILL_MDC : Terminates the current running MDC project.
LOAD $path_to_mdc_project_or_playlist : Load and start project/playlist
AULOAD $path_to_mdc_automatic : Load and start automatic file
KILL_AUTO : Kill all automatic jobs
LAMP_ON $MIRROR_ID : Projector lamp on
LAMP_OFF $MIRROR_ID : Projector lamp off
MOTOR_OFF $MIRROR_ID : Mirror Head Motor&LED off
MOTOR_ON $MIRROR_ID : Mirror Head Motor&LED off
RESET $MIRROR_ID : Mirror Head Reset
SCREENSETUP : Request restart of screen detection (== CRTL+ALT+SHIFT+S)
MDC_REBOOT : Request MDC reboot (== CRTL+ALT+SHIFT+R)
MDC_HALT : Request HALT of MDC
SYSTEM_SHUTDOWN $MIRROR_ID : Combination of KILL_MDC + LAMP_OFF + MOTOR_OFF
SYSTEM_START $MIRROR_ID : Combination of KILL_MDC + LAMP_ON + MOTOR_ON
MODE_MANUAL : Enable manual control
MODE_AUTOMATIC : Disable manual control
DLOAD : Load default project - can be set in the SETUP page of MDC-Touch
DAULOAD : Load default automatic - can be set in the SETUP page of MDC-Touch
SIMPLESTART: This is equal to the TURN ON button on MDC-Touch
SIMPLEKILL: This is equal to the TURN OFF button on MDC-Touch
'''


#Load AUTOMATIC  - configure in MDC-Touch SETUP
print "Loading DEFAULT project...."
syssender(mdcx_system,"DLOAD  0")
time.sleep(10)
print "Loading DEFAULT automatic...."
syssender(mdcx_system,"DAULOAD  0")
time.sleep(30)
print "Stopping DEFAULT automatic and SHOW...."
syssender(mdcx_system,"KILL_MDC 0")
syssender(mdcx_system,"KILL_AUTO 0")
print "End of DEMONSTRATION"


