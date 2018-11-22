# Hello World program in Python
#import pytz
import sys
import datetime
import logging
import binascii
from struct import unpack




#print (a[0])
#b=a[0]
msg = bytearray()
#b=a[0]
print (len(a))
for x in range (len(a)):
    #print(a[x])
    #b +=a[x]
    msg.extend(a[x])
#a = a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
a= msg
users = {}
if len(a) > 0:
	#for x in range(len(a)):
		userdata = a
		#print x
		userdata = userdata[11:]
		while len(userdata) > 72:
			#print (len(userdata))
			uid, role, password, name, userid = unpack('2s2s8s28sx31s', userdata.ljust(72)[:72])
			uid = int(binascii.hexlify(uid), 16)
			print ("uid " + str(uid))
			# Clean up some messy characters from the user name
			
			password = password.split(b'\x00', 1)[0]
			print ("password "+ str(password))
			password = str(password.strip(b'\x00|\x01\x10x|\x000').decode('utf-8'))
			print ("password "+ str(password))
			# uid = uid.split('\x00', 1)[0]
			print ("userid "+ str(userid))
			print ("userid "+ str(userid.strip(b'\x00|\x01\x10x|\x000|\x9aC')))
			userid = str(userid.strip(b'\x00|\x01\x10x|\x000|\x9aC').decode('ISO-8859-1'))
			print ("userid **** "+ str(userid))
			name = name.split(b'\x00', 1)[0].decode('utf-8')
			if name.strip() == "":
				name = uid
			print ("name **** "+ str(name))
			users[uid] = (userid, name, int(binascii.hexlify(role), 16), password)
			userdata = userdata[72:]
			
		print (users)
		
