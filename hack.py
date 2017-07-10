#!/usr/bin/python

import sys
from time import sleep
from datetime import datetime

if len(sys.argv) < 2:
	print 'Error: please enter target'
	sys.exit()

target = sys.argv[1]

sleep(3)
print '\033[1m\033[94m[*]\033[0m Sending stage (748544 bytes) to %s' % target
sleep(0.75)
timestamp = datetime.now()
print '\033[1m\033[94m[*]\033[0m Meterpreter session 1 opened (localhost:39625 -> %s:80) at %s\n' % (target, timestamp)
sleep(0.25)

def exit():
	print "\033[1m\033[94m[*]\033[0m Shutting down Meterpreter..."
	sleep(0.5)
	print "\n\033[1m\033[94m[*]\033[0m %s - Meterpreter session 1 closed.  Reason: User exit" % target

try:
	while True:
		sys.stdout.write("\033[4mmeterpreter\033[0m > ")
		input = raw_input()
		if input == '':
			sys.stdout.write('')
		elif input == "exit":
			exit()
			break
		else:
			sleep(1.5)
			print '\033[1m\033[91m[-]\033[0m Error running command %s: Rex::TimeoutError Operation timed out.' % input
except:
	print ''
	exit()
