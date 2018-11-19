import pytz
import sys
import datetime
import logging
import binascii
#import sys
from zklib import zklib

import time
from zklib import zkconst
#from .zkconst import *
from struct import unpack
zk = zklib.ZKLib("10.10.10.26", 4370)
#print (zk)
#conn = self.device_connect(zk)
'''

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


def getSizeUser(self, zk):
	"""Checks a returned packet to see if it returned CMD_PREPARE_DATA,
	indicating that data packets are to be sent

	Returns the amount of bytes that are going to be sent"""
	command = unpack('HHHH', zk.data_recv[:8])[0]
	if command == CMD_PREPARE_DATA:
		size = unpack('I', zk.data_recv[8:12])[0]
		return size
	else:
		return False

def zkgetuser(self, zk):
	"""Start a connection with the time clock"""
	command = CMD_USERTEMP_RRQ
	command_string = '\x05'
	chksum = 0
	session_id = zk.session_id
	reply_id = unpack('HHHH', zk.data_recv[:8])[3]

	buf = zk.createHeader(command, chksum, session_id, reply_id, command_string)
	zk.zkclient.sendto(buf, zk.address)
	try:
		zk.data_recv, addr = zk.zkclient.recvfrom(1024)

		if self.getSizeUser(zk):
			bytes = self.getSizeUser(zk)

			while bytes > 0:
				data_recv, addr = zk.zkclient.recvfrom(1032)
				zk.userdata.append(data_recv)
				bytes -= 1024

			zk.session_id = unpack('HHHH', zk.data_recv[:8])[2]
			data_recv = zk.zkclient.recvfrom(8)

		users = {}
		if len(zk.userdata) > 0:
			userdata = zk.userdata[0]
			userdata = userdata[11:]
			while len(userdata) > 72:
				uid, role, password, name, userid = unpack('2s2s8s28sx31s', userdata.ljust(72)[:72])
				uid = int(binascii.hexlify(uid), 16)
				# Clean up some messy characters from the user name
				password = password.split(b'\x00', 1)[0]
				password = str(password.strip(b'\x00|\x01\x10x|\x000').decode('utf-8'))
				# uid = uid.split('\x00', 1)[0]
				userid = str(userid.strip(b'\x00|\x01\x10x|\x000|\x9aC').decode('utf-8'))
				name = name.split(b'\x00', 1)[0].decode('utf-8')
				if name.strip() == "":
					name = uid
				users[uid] = (userid, name, int(binascii.hexlify(role), 16), password)
				userdata = userdata[72:]
		return users
	except:
		return False'  
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
	#print(command+"")
	if command == 2000:
		conn = True
	else:
		conn = False
	print conn
except:
	conn = False
if conn:
	print ("getUser")
	zk.enableDevice()
	"""Start a connection width the time clfk"""
	command = 9
	command_string = '\x05'
	chksum = 0
	session_id = zk.session_id
	reply_id = unpack('HHHH', zk.data_recv[:8])[3]

	buf = zk.createHeader(command, chksum, session_id, reply_id, command_string)
	zk.zkclient.sendto(buf, zk.address)
	try:
		zk.data_recv, addr = zk.zkclient.recvfrom(1024)
		#zk.userdata = bytearray()
		userdata = bytearray()
		command = unpack('HHHH', zk.data_recv[:8])[0]
		if command == 1500:
			size = unpack('I', zk.data_recv[8:12])[0]
			size = size
		else:
			size =  False
		print ("size = "+str(size))

		if size:
			bytes = size
			##bytes = 4096
			print ("bytes = "+str(bytes))
			print ("******")
			while bytes > 0:
				#print ("******")
				data_recv, addr = zk.zkclient.recvfrom(1032)
				#print (data_recv)
				#print (addr)
				zk.userdata.append(data_recv)
				#print ("***zk.userdata***")
				#print (zk.userdata)
				bytes -= 1024
			#print (zk.userdata[:2])	
			zk.session_id = unpack('HHHH', zk.data_recv[:8])[2]
			data_recv = zk.zkclient.recvfrom(8)
			print (len(zk.userdata))
			#print (zk.userdata)#MMMM

		users = {}
		#userdata = bytearray()
		if len(zk.userdata) > 0:
			# The first 4 bytes don't seem to be related to the use.r.
			for x in range(len(zk.userdata)):
				if x > 0:
					zk.userdata[x] = zk.userdata[x][8:]	
					#userdata = userdata.extend(zk.userdata[x])
					
			#userdata = ''.join( zk.userdata )
			#print(zk.userdata[0])
			userdata = userdata.extend(zk.userdata)
			#userdata = zk.userdata
			print (userdata[:2])
			userdata = userdata[11:]
			while len(userdata) > 72:
				uid, role, password, name, userid = unpack('2s2s8s28sx31s', userdata.ljust(72)[:72])
				uid = int(binascii.hexlify(uid), 16)
				# Clean up some messy characters from the user name
				password = password.split(b'\x00', 1)[0]
				password = str(password.strip(b'\x00|\x01\x10x|\x000').decode('utf-8'))
				# uid = uid.split('\x00', 1)[0]
				userid = str(userid.strip(b'\x00|\x01\x10x|\x000|\x9aC').decode('utf-8'))
				name = name.split(b'\x00', 1)[0].decode('utf-8')
				if name.strip() == "":
					name = uid
				users[uid] = (userid, name, int(binascii.hexlify(role), 16), password)
				userdata = userdata[72:]
		print (users)
	except:
		print (False)  
	
	
	#user = zkgetuser(zk)
	
zk.enableDevice()
zk.disconnect()

