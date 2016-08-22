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
numPrefLevels = input["NumPrefLevels"]
numTracks = input["NumTracks"]

sectionsKey = input["SectionsKey"]
classesKey = input["ClassesKey"]
studentsKey = input["StudentsKey"]

allPrefs = {}

classScores = [[0 for i in range(0,numClasses)] for j in range(0,numSections)]

for studentNum in range(0,numStudents):
	#print str(studentNum) + ":"
	#print input[studentsKey][str(studentNum)][classesKey]
	#print input[studentsKey][str(studentNum)][sectionsKey]
	for classNum in range(0,numClasses):
		for sectionNum in range(0,numSections):
			if(input[studentsKey][str(studentNum)][str(sectionsKey)][str(sectionNum)] == 1):
				classScores[classNum][sectionNum] += input[studentsKey][str(studentNum)][str(classesKey)][str(classNum)]


print classScores
		

