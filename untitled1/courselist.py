from lxml import html
import requests as r
import unicodedata
import pandas as p
import sys
import csv
import os



def getCourseInfo(course):
    '''
        with open('data.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            id = []
            course_name = []
            for row in readCSV:
                id.append(row[0])
                course_name.append(row[1])
            try:
                return course_name[id.index(course)]
            except:
                return "Doesn't exist"
    '''
    workpath = os.path.dirname(os.path.abspath(__file__))

    data = p.read_csv(os.path.join(workpath, 'data.csv'))
    x = data.set_index("ID").T.to_dict('list')
    try:
        coursedata = x[course]
        return coursedata[0], coursedata[1]
    except:
        return "Course " + course + " doesn't exist. "

##rowfound = data.loc[data["ID"] == "CS 1331"]
'''
x = input("Type a course ID!!!")
print(getCourseInfo(x))

'''
