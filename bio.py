import pytz
import sys
import datetime
import logging
import binascii
#import sys
from zklib import zklib

import time
from zklib import zkconst
from struct import unpack
zk = zklib.ZKLib("10.10.10.26", 4370)
#conn = self.device_connect(zk)
''''

res = zk.connect()
if res == True:
	print zk.enableDevice()
	print zk.disableDevice()
	print zk.version()
	print zk.osversion()
	print zk.deviceName()
	print (zk.getUser())
	zk.enableDevice()
	zk.disconnect()
'''
command = 1000
command_string = ''
chksum = 0
session_id = 0
reply_id = -1 + 65535
buf = zk.createHeader(command, chksum, session_id,
					  reply_id, command_string)
zk.zkclient.sendto(buf, zk.address)
try:
	zk.data_recv, addr = zk.zkclient.recvfrom(1024)
	zk.session_id = unpack('HHHH', zk.data_recv[:8])[2]
	command = unpack('HHHH', zk.data_recv[:8])[0]
	print(command+"")
	if command == 2000:
		conn = True
	else:
		conn = False
	print conn
except:
	conn = False
zk.enableDevice()
zk.disconnect()

