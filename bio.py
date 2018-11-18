import pytz
import sys
import datetime
import logging
import binascii

from zklib import zklib, zkconst
from struct import unpack
zk = zklib.ZKLib('10.10.10.26', '4370')

res = zk.connect()
if res == True:
	print zk.enableDevice()
	print zk.disableDevice()
	print zk.version()
	print zk.osversion()
	print zk.deviceName()
	#zk.getUser()
	#zk.enableDevice()
	#zk.disconnect()