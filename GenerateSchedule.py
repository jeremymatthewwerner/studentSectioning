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

for student in AllPrefs[studentsKey]:
	print student

