#!/usr/bin/python
import xml.etree.ElementTree as ET
import glob
import os

labelString = ''

#create trainBear.txt
for py in glob.glob("bearImages/images/train/*"):
	labelString = labelString + "\n" +"../"+ py

newFile = open("trainBear.txt", "w+")
newFile.write(labelString)
newFile.close()

labelString = ''

#create testBear.txt
for py in glob.glob("bearImages/images/val/*"):
	labelString = labelString + "\n" +"../"+ py

newFile = open("testBear.txt", "w+")
newFile.write(labelString)
