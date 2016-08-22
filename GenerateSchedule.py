#!/usr/bin/python

import sys
import json
import random
import numpy as np

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

schedule = [[-1 for i in range(0,numTracks)] for j in range(0, numSections)]

for studentNum in range(0,numStudents):
	for classNum in range(0,numClasses):
		for sectionNum in range(0,numSections):
			if(input[studentsKey][str(studentNum)][str(sectionsKey)][str(sectionNum)] == 1):
				classScores[sectionNum][classNum] += input[studentsKey][str(studentNum)][str(classesKey)][str(classNum)]	

print classScores

for sectionNum in range(0,numSections):
	arr = np.array(classScores[sectionNum])
	top3 = arr.argsort()[numTracks*-1:][::-1]
	for trackNum in range(0, numTracks):
		schedule[sectionNum][trackNum] = top3[trackNum]

print schedule



		

