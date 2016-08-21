#!/usr/bin/python

import sys
import json
import random

def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))

random.seed()

with open(sys.argv[1]) as data_file:    
    input = json.load(data_file)

numClasses = input["NumClasses"]
numSections = input["NumSections"]
numStudents= input["NumStudents"]
numPrefs = input["NumPrefs"]

classSections = {}


classSectionID = 0;
for classNum in range(0,numClasses):
	for sectionNum in range(0,numSections):
		classSectionDict = {'classNum':classNum, 'sectionNum':sectionNum}
		classSections[classSectionID] = classSectionDict
		classSectionID+=1

random.shuffle(classSections)

classSectionJson = json.dumps(classSections)

print get_pretty_print(classSectionJson)
