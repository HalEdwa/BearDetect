#!/usr/bin/python
import xml.etree.ElementTree as ET
import glob
import os
#oldFile = open(oldfilename, "r")
#linesOfFile = oldFile.read()
#xmlRoot = ET.fromstring(linesOfFile)

def modifyTxtFile(fileName):
	#pull out data
	#oldLabelPath = "bearImages/HigherBearImages/Labels/"
	newLabelPath = "bearImages/labels/"
	xmlData = ET.parse(fileName)
	xmlObject = xmlData.find('object')
	xmlBndBox = xmlObject.find('bndbox')
	xmin = int(xmlBndBox.find('xmin').text)
	xmax = int(xmlBndBox.find('xmax').text)
	ymin = int(xmlBndBox.find('ymin').text)
	ymax = int(xmlBndBox.find('ymax').text)

	xmlSize = xmlData.find('size')
	width = int(xmlSize.find('width').text)
	height = int(xmlSize.find('height').text)

	# create correct values
	xCenter = round((float(xmin+xmax)/2)/width,6) 
	yCenter = round((float(ymin+ymax)/2)/height,6)

	boxWidth = round(float(xmax-xmin)/width,6)
	boxHeight = round(float(ymax-ymin)/height,6)

	#save to new file
	newDataString = "0 " + str(xCenter) + " " + str(yCenter) + " " + str(boxWidth) + " " + str(boxHeight)
	head, tail = os.path.split(fileName)
	newFile = open(newLabelPath+tail[:-3]+"txt", "w+")
	newFile.write(newDataString)


for py in glob.glob("bearImages/BearMaskLabeledPhotos/Labels/*.xml"):
	modifyTxtFile(py)
