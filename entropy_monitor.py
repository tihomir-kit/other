import sys, time

while True:
	sys.stdout.write(open('/proc/sys/kernel/random/entropy_avail', 'r').read())
	time.sleep(1)
