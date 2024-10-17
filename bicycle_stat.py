#!/usr/bin/python3

# rad_werner_1.py
# do some plots for the bicycle km per month / over years
# read data from xml file defined with IN_FILENAME
# Werner Schoegler, 8-2024

IN_FILENAME = "bicycle_training.xml"

import matplotlib.pyplot as plt
import numpy as np
import xml.dom.minidom

class distanceEntry:
    def __init__(self, year, month, distance):
        self.year = year
        self.month = month
        self.distance = distance
    def print(self):
        print(f"{self.year},{self.month},{self.distance}")

class alldDistanceEntries:
    def __init__(self):
        self.distancePerMonthList = []

    # add data for selected month/year
    def addToDistancePerMonthList(self, year, month, distance):
        myDistanceEntry = distanceEntry(year, month, distance)
        self.distancePerMonthList.append(myDistanceEntry)
    
    # add data for a specific year
    def addYear(self, data):
        year=data[0]
        self.addToDistancePerMonthList(year, 1,   data[1])
        self.addToDistancePerMonthList(year, 2,   data[2])
        self.addToDistancePerMonthList(year, 3,   data[3])
        self.addToDistancePerMonthList(year, 4,   data[4])
        self.addToDistancePerMonthList(year, 5,   data[5])
        self.addToDistancePerMonthList(year, 6,   data[6])
        self.addToDistancePerMonthList(year, 7,   data[7])
        self.addToDistancePerMonthList(year, 8,   data[8])
        self.addToDistancePerMonthList(year, 9,   data[9])
        self.addToDistancePerMonthList(year,10,   data[10])
        self.addToDistancePerMonthList(year,11,   data[11])
        self.addToDistancePerMonthList(year,12,   data[12])
    
    # get sum of kilometers in year
    def getDistanceInYear(self, year):
        sumYear=0
        for elem in self.distancePerMonthList:
            if elem.year==year:
                sumYear+=elem.distance
        return sumYear 

    # get list with kilometers per month of selected year
    def getDistanceListInYear(self, year):
        distanceList=[]
        for elem in self.distancePerMonthList:
            if elem.year==year:
                distanceList.append(elem.distance)
        return distanceList                 

# get the data for each month into a list return value
def getData(year, elem):
    data = [int(year)]
    data.append(int(elem.getElementsByTagName('JAN')[0].childNodes[0].data))
    data.append(int(elem.getElementsByTagName('FEB')[0].childNodes[0].data))
    data.append(int(elem.getElementsByTagName('MAR')[0].childNodes[0].data))
    data.append(int(elem.getElementsByTagName('APR')[0].childNodes[0].data))
    data.append(int(elem.getElementsByTagName('MAY')[0].childNodes[0].data))
    data.append(int(elem.getElementsByTagName('JUN')[0].childNodes[0].data))
    data.append(int(elem.getElementsByTagName('JUL')[0].childNodes[0].data))
    data.append(int(elem.getElementsByTagName('AUG')[0].childNodes[0].data))
    data.append(int(elem.getElementsByTagName('SEP')[0].childNodes[0].data))
    data.append(int(elem.getElementsByTagName('OCT')[0].childNodes[0].data))
    data.append(int(elem.getElementsByTagName('NOV')[0].childNodes[0].data))
    data.append(int(elem.getElementsByTagName('DEC')[0].childNodes[0].data))
    return data

# ===== M A I N program
# entry of data points from xml file

DOMTree = xml.dom.minidom.parse(IN_FILENAME)

# get DOM element that contain the actual XML data
bicycleTraining = DOMTree.documentElement
print(f"bicycleTraining: {bicycleTraining}")

# now get all yearentry elements
yearEntries = bicycleTraining.getElementsByTagName("YEARENTRY")
print(f"yearEntries: {yearEntries}")

myDiEntries = alldDistanceEntries()
# process each element inside yearEntries for parsing data
for elem in yearEntries:
    yearElem = elem.getElementsByTagName('YEAR')[0]
    year = yearElem.childNodes[0].data
    data = getData(year, elem)
    print(data)
    myDiEntries.addYear(data)

# generate lists for plot per month
xlist = range(1,12)
ylist21 = myDiEntries.getDistanceListInYear(2021)
ylist22 = myDiEntries.getDistanceListInYear(2022)
ylist23 = myDiEntries.getDistanceListInYear(2023)
ylist24 = myDiEntries.getDistanceListInYear(2024)

# now do the plot
fig, ax = plt.subplots()
x = np.arange(12) 
width = 0.15
ax.grid(which='major', axis='y', linestyle='-')
plt.bar(x+1-0.4, ylist21, width, color='grey') 
plt.bar(x+1-0.2, ylist22, width, color='lightgrey') 
plt.bar(x+1,      ylist23, width, color='orange') 
plt.bar(x+1+0.2, ylist24, width, color='dodgerblue') 
plt.legend(["2021","2022", "2023", "2024"]) 
ax.set_xlabel('month')
ax.set_ylabel('distance')
ax.set_title('bicycle distance per month over years')
plt.show()

# generate lists for plot over years
yearsToShow = [2019, 2020, 2021, 2022, 2023, 2024]
x=[]
y=[]
for year in yearsToShow:
    x.append(f"{year}")
    y.append(myDiEntries.getDistanceInYear(year))

# now do the 2nd plot
fig, ax = plt.subplots()
ax.grid(which='major', axis='x', linestyle='-')
ax.set_xlabel('year')
ax.set_ylabel('distance')
ax.set_ylim([0, 5000])
ax.grid()
plt.bar(x,y, 0.4, color='dodgerblue')
plt.title('bicycle kilometers over years')
plt.show()






