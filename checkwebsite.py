from urllib2 import urlopen, HTTPError

from socket import timeout


try:
	data = urlopen('http://www.alumnimeet.iitkgp.ernet.in',timeout = 5)
	print data.getcode()
except HTTPError:
	print data.getcode()
except timeout:
	print "It is taking very long to connect to the ALUMNIMEET website. Look into it."

try:
	data2 = urlopen('http://www.mentorship.iitkgp.ernet.in',timeout = 5)
	print data.getcode()
except HTTPError:
	print data.getcode()
except timeout:
	print "It is taking very long to connect to the MENTORSHIP website. Look into it."



