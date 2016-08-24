# studentSectioning
code to optimize a home schooling class schedule given student preferences for class and timeslot

# To generate some fake preferences and then create and score a schedule from them, do this:

pip install simanneal  # from pypi

./GenerateStudentPrefs2.py ./StudentPrefsGenParams.json > ./data2.json ;./GenerateSchedule.py ./data2.json
