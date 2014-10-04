import datetime
import csv
from matplotlib import pyplot as plt

f = open('results.csv','rb')
reader = csv.reader(f,delimiter=' ', quotechar='|')

timestamps = []
values = []

for row in reader:
	timestamps.append(row[0]+' '+row[1])
	values.append(row[2])

for i in range(len(values)):

	values[i] = 1024/float(values[i])

print values

for i in range(len(timestamps)):
	timestamps[i] = datetime.datetime.strptime(timestamps[i], "%Y-%m-%d %H:%M:%S.%f")



plt.plot(timestamps,values,marker='.',lw=3,color="red")

plt.gca().set_ylim([0,200])
plt.gcf().autofmt_xdate()

plt.fill_between(timestamps,0,values,facecolor='red', alpha=0.5)


plt.show()
