#!/usr/bin/python

import sys
import json
import random

import pprint


def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))

random.seed()

with open(sys.argv[1]) as data_file:    
    input = json.load(data_file)

numClasses = input["NumClasses"]
numSections = input["NumSections"]
numStudents= input["NumStudents"]
numPrefs = input["NumPrefs"]

classSectionPrefix = "Class Section "
prefrencePrefix = "Preference "
studentPrefix = "Student "


classSections = {}


classSectionID = 0;
for classNum in range(0,numClasses):
	for sectionNum in range(0,numSections):
		classSectionDict = {'classNum':classNum, 'sectionNum':sectionNum}
		classSections[classSectionPrefix + str(classSectionID)] = classSectionDict
		classSectionID+=1

allPrefs = {}

for studentNum in range(0,numStudents):

	items=classSections.items() # List of tuples
	random.shuffle(items)

	prefs = {}
	morePrefs = numPrefs
	prefId = 0
	for key, value in items:
		if(morePrefs > 1):
			prefs[prefrencePrefix + str(prefId)] = {str(key):str(value)}
			prefId+=1
		morePrefs-=1
	allPrefs[studentPrefix + str(studentNum)] = prefs

#print(allPrefs)

allPrefs["NumClasses"] = numClasses;
allPrefs["NumSections"] = numSections;
allPrefs["NumPrefs"] = numPrefs;
allPrefs["ClassSectionPrefix"] = classSectionPrefix;
allPrefs["PrefrencePrefix"] = prefrencePrefix;
allPrefs["StudentPrefix"] = studentPrefix;


classSectionJson = json.dumps(allPrefs, indent=4, sort_keys=True)

print classSectionJson


