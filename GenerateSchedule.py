#!/usr/bin/python

import sys
import json
import random
import numpy as np

import pprint

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

def get_pretty_print(json_object):
	return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))

def studentScheduleScore(student, schedule):
	return 3

def scheduleScore(schedule, inputJson):
	scores = []
	for studentNum in range(0,numStudents):
		scores.append(studentScheduleScore(inputJson[studentsKey][str(studentNum)], schedule))
	return np.mean(scores)

random.seed()

allPrefs = {}

# Build an initial schedule out of most popular classes (1st track highest rated, 2nd 2nd, etc.)

classScores = [[0 for i in range(0,numClasses)] for j in range(0,numSections)]

schedule = [[-1 for i in range(0,numTracks)] for j in range(0, numSections)]

for studentNum in range(0,numStudents):
	for classNum in range(0,numClasses):
		for sectionNum in range(0,numSections):
			if(input[studentsKey][str(studentNum)][str(sectionsKey)][str(sectionNum)] == 1):
				classScores[sectionNum][classNum] += input[studentsKey][str(studentNum)][str(classesKey)][str(classNum)]	

#print classScores

for sectionNum in range(0,numSections):
	arr = np.array(classScores[sectionNum])
	top3 = arr.argsort()[numTracks*-1:][::-1]
	for trackNum in range(0, numTracks):
		schedule[sectionNum][trackNum] = top3[trackNum]

print "Schedule:" + str(schedule)

print "Schedule score: " + str(scheduleScore(schedule, input))
