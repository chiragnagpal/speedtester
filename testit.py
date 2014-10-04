import csv
from datetime import datetime
import time
import requests

main_time_prev = 0

f = open('results.csv','wb')
writer = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_ALL)
url = "http://androidnetworktester.googlecode.com/files/1mb.txt"
while 1:
	
	if (time.time() - main_time_prev) > 210 :
		main_time_prev = time.time()
		print "start"
		l = []
		
		l=l+str(datetime.now()).split(' ')
		
		
		print "download start"
		t1 = time.time()
		try:
			r = requests.get(url)	

		
			t2 = time.time()
			
			l.append(t2 - t1)		
		except :
			continue

		print l
		writer.writerow(l)
		
