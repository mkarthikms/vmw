import socket
import time
from urllib2 import urlopen

URLS = ['https://httpstat.us/200', 'https://httpstat.us/503']
socket.setdefaulttimeout( 15 )  # timeout in seconds

for url in URLS:
    start = time.clock()
    try:
        response = urlopen(url)
        if (response.getcode() ==  200):
           print 'sample_external_url_up {0} = 1'
           print 'sample_external_url_up {0} = {0}s\n'.format(time.clock() - start)'
        elif (response.getcode() ==  503):
           print 'sample_external_url_up {1} = 0'
           print 'sample_external_url_up {1} = {1}s\n'.format(time.clock() - start)'
        else:
	   print ''
   
    except StandardError, e:
        print ''
