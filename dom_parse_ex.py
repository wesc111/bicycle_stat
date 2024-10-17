
# dom_parse3.py

import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("bicycle_training.xml")

# get DOM element that contain the actual XML data
bicycleTraining = DOMTree.documentElement
print(f"bicycleTraining: {bicycleTraining}")

# now get all yearentry elements
yearEntries = bicycleTraining.getElementsByTagName("YEARENTRY")
print(f"yearEntries: {yearEntries}")

# get the data for each month into a list return value
def getData(elem):
    data = []
    data.append(elem.getElementsByTagName('JAN')[0].childNodes[0].data)
    data.append(elem.getElementsByTagName('FEB')[0].childNodes[0].data)
    data.append(elem.getElementsByTagName('MAR')[0].childNodes[0].data)
    data.append(elem.getElementsByTagName('APR')[0].childNodes[0].data)
    data.append(elem.getElementsByTagName('MAY')[0].childNodes[0].data)
    data.append(elem.getElementsByTagName('JUN')[0].childNodes[0].data)
    data.append(elem.getElementsByTagName('JUL')[0].childNodes[0].data)
    data.append(elem.getElementsByTagName('AUG')[0].childNodes[0].data)
    data.append(elem.getElementsByTagName('SEP')[0].childNodes[0].data)
    data.append(elem.getElementsByTagName('OCT')[0].childNodes[0].data)
    data.append(elem.getElementsByTagName('NOV')[0].childNodes[0].data)
    data.append(elem.getElementsByTagName('DEC')[0].childNodes[0].data)
    return data

# process each element inside yearEntries for parsing data
for elem in yearEntries:
    yearElem = elem.getElementsByTagName('YEAR')[0]
    year = yearElem.childNodes[0].data
    data = getData(elem)
    print(yearElem,year,data)
