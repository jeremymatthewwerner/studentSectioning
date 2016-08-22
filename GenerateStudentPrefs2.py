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

studentPrefix = "Student "
sectionPrefix = "Section "
classPrefix = "Class "
sectionsKey = "Sections"
classesKey = "Classes"

allPrefs = {}

allPrefs["NumClasses"] = numClasses;
allPrefs["NumSections"] = numSections;
allPrefs["NumStudents"] = numSections;
allPrefs["NumPreflevels"] = numPrefLevels;
allPrefs["NumTracks"] = numTracks;

allPrefs["StudentPrefix"] = studentPrefix;
allPrefs["SectionPrefix"] = sectionPrefix;
allPrefs["ClassPrefix"] = classPrefix;
allPrefs["SectionsKey"] = sectionsKey;
allPrefs["ClassesKey"] = classesKey;

for studentNum in range(0,numStudents):

	sections = {}

	classes = {}

	for sectionNum in range(0,numSections):
		sections[sectionPrefix + str(sectionNum)] = random.randint(0,1)

	for sectionNum in range(0,numClasses):
		classes[classPrefix + str(sectionNum)] = random.randint(0,numPrefLevels)

	allPrefs[studentPrefix + str(studentNum)] = {}
	allPrefs[studentPrefix + str(studentNum)][sectionsKey] = sections
	allPrefs[studentPrefix + str(studentNum)][classesKey] = classes

allPrefsJson = json.dumps(allPrefs, indent=4, sort_keys=True)

print allPrefsJson
	

