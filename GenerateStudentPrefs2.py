#!/usr/bin/python

import sys
import json
import random

random.seed()

with open(sys.argv[1]) as data_file:    
    input = json.load(data_file)

numClasses = input["NumClasses"]
numSections = input["NumSections"]
numStudents= input["NumStudents"]
numPrefLevels = input["NumPrefLevels"]
numTracks = input["NumTracks"]

sectionsKey = "Sections"
classesKey = "Classes"
studentsKey = "Students"

allPrefs = {}

allPrefs["NumClasses"] = numClasses;
allPrefs["NumSections"] = numSections;
allPrefs["NumStudents"] = numStudents;
allPrefs["NumPrefLevels"] = numPrefLevels;
allPrefs["NumTracks"] = numTracks;

allPrefs["SectionsKey"] = sectionsKey;
allPrefs["ClassesKey"] = classesKey;
allPrefs["StudentsKey"] = studentsKey;

allPrefs[studentsKey] = {}

for studentNum in range(0,numStudents):

	sections = {}
	for sectionNum in range(0,numSections):
		sections[str(sectionNum)] = random.randint(0,1)

	classes = {}
	for sectionNum in range(0,numClasses):
		classes[str(sectionNum)] = random.randint(0,numPrefLevels-1)

	allPrefs[studentsKey][str(studentNum)] = {}
	allPrefs[studentsKey][str(studentNum)][sectionsKey] = sections
	allPrefs[studentsKey][str(studentNum)][classesKey] = classes

allPrefsJson = json.dumps(allPrefs, indent=4, sort_keys=True)

print allPrefsJson

