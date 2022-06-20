
#############################################################################################
# This file allows ploting the signals of the dataset
#
# Author: Pedro Merino Laso
# License: Creative Commons Attribution-ShareAlike 4.0 International License
#
##############################################################################################

import csv
import matplotlib.pyplot as plt
import tkFileDialog
from math import log


filename = tkFileDialog.askopenfilename(title="Select a log:", initialdir="./", filetypes = [("Log files","*.csv"),("All", "*")])

cr = csv.reader(open(filename,"rb"))


time1 = []
sensorIN2 = []
sensorIN1 = []
sensorIN0 = []
sensorIN3 = []

time3 = []
sensorPP = []
sensorPG = []
sensorVP = []
sensorVG = []
alarm  = []

time2 = []
sounder = []

#Pruebas

time_max = 0.0

first = True
second = True

for row in cr:
	if first:
		first = False
	else:
		if row[1] in ("2", "3", "4"):
			time = (float(row[0][11:13])*60 + float(row[0][14:16]))*60 + float(row[0][17:23])
			if second:
				second = False
				time_inicial = time

			time = time - time_inicial

			if row[1] == "2":
				captores = format(int(row[2]), '08b')
				sensorIN3.append(captores[4])
				sensorIN2.append(captores[5])
				sensorIN1.append(captores[6])
				sensorIN0.append(captores[7])
				time1.append(time)
				if time > time_max:
					time_max = time
			elif row[1] == "3":
				captores = format(int(row[2]), '08b')
				sensorPP.append(captores[0])
				sensorPG.append(captores[1])
				sensorVP.append(captores[5])
				sensorVG.append(captores[4])
				alarm.append(captores[3])
				time3.append(time)
				if time > time_max:
					time_max = time
			elif row[1] == "4":
				sounder.append(int(row[2]))
				time2.append(time)
				if time > time_max:
					time_max = time



#PLOTS
nfigures = 4

plt.subplot(nfigures,1,1)
plt.plot(time2, sounder, label="Depth sounder")
plt.axis([0, time_max, -10, 10100])
plt.legend(loc='upper left')

# Main tank
plt.subplot(nfigures,1,2)
plt.plot(time3, sensorPP, label="Pump 2")
plt.plot(time3, sensorVP, label="Valve_main")
plt.axis([0, time_max, -0.1, 1.1])
plt.legend(loc='upper left')


#Discrete sensors
plt.subplot(nfigures,1,3)
plt.plot(time1, sensorIN0, label="IN0")
plt.plot(time1, sensorIN1, label="IN1")
plt.plot(time1, sensorIN2, label="IN2")
plt.plot(time1, sensorIN3, label="IN3")
plt.axis([0, time_max, -0.1, 1.1])
plt.legend(loc='upper left')

# Secondary tank
plt.subplot(nfigures,1,4)
plt.plot(time3, sensorPG, label="Pump 1")
plt.plot(time3, sensorVG, label="Valve_secondary")
plt.axis([0, time_max, -0.1, 1.1])
plt.legend(loc='upper left')

plt.show()


