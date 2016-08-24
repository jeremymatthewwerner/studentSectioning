#!/usr/bin/python

# psudo-optimal blocked class scheduling
# higher student class ratings are higher
# 1 means student can takes classes during a block, 0 means cannot
# lower per-student schedules are higher

import sys
import json
import random
import numpy as np
from operator import itemgetter

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

def studentScheduleScore(student, schedule, studentNum):
	#print "Student:" + str(studentNum)
	rankedClasses = sorted(student[str(classesKey)].items(), key=itemgetter(1), reverse=True)

	score = 0; # 0 is a perfect score
	cost = len(rankedClasses)

	for rankedEntry in rankedClasses:
		rankedClass = int(rankedEntry[0])

		found = 0
		atLeastOneSection = 0
		for sectionNum in range(0,numSections):
			if(student[str(sectionsKey)][str(sectionNum)] == 1):
				atLeastOneSection = 1
				#print "TODO: Check schedule tracks for class " + str(rankedClass) + " in section " + str(sectionNum)
				if rankedClass in schedule[sectionNum]:
					found = 1
		
		if(atLeastOneSection == 0):
			print "ERROR: Student " + str(studentNum) + " chose no sections so their score will skew the result!"
		
		if(found==0):
			score += cost	
			#print "deducted " + str(cost) + " for new score " + str(score) + ", did not find " + str(rankedClass) + " in any sections the student can attend"

		cost -= 1

	return score

def scheduleScore(schedule, inputJson):
	scores = []
	for studentNum in range(0,numStudents):
		score = studentScheduleScore(inputJson[studentsKey][str(studentNum)], schedule, studentNum)
		print "Student " + str(studentNum) + ": " + str(score)
		scores.append(score)
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
