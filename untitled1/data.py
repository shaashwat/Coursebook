from lxml import html
import requests as r
import unicodedata
from pandas import DataFrame
import os
import csv
cwd = os.getcwd()
page = r.get("http://www.catalog.gatech.edu/coursesaz/")
tree = html.fromstring(page.content)

a_to_z_list = tree.xpath('//div[@id="atozindex"]')[0]

course_category_links = a_to_z_list.xpath('.//a//@href')

courses_raw = []
course_id = []
course_name = []
course_credits = []
course_desc = []

for course_link in course_category_links:
    page2 = r.get("http://www.catalog.gatech.edu" + course_link)
    tree2 = html.fromstring(page2.content)
    id_name_credit = tree2.xpath('//p[@class="courseblocktitle"]/strong/text()')
    for course in id_name_credit:
        course = unicodedata.normalize("NFKD", course)
        course_id.append(course[0:course.find('.')])
        course = course[course.find('.') + 3:]
        course_name.append(course[0:course.find('.')])
        course = course[course.find('.') + 3:]
        course_credits.append(course[0:1])

course_info = {'ID': course_id,
               'Name': course_name,
               'Credit Hours': course_credits,
               'Description': course_desc}

df = DataFrame(course_info, columns=['ID', 'Name', 'Credit Hours', 'Description'])
print(df)


export_csv = df.to_csv("data2.csv", index = None, header = True)
'''
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Credit Hours"])
    writer.writerows(df)
'''