from __future__ import absolute_import
from lxml import html
import requests as r
#from pandas import DataFrame
from .rmp.RMPClass import RateMyProfScraper
#import fileinput
#import os

#cwd = os.getcwd()
GeorgiaTech = RateMyProfScraper(361)
def setupRMP():
    print('reached')
    return None

def getProfComments(profname):
    profname = ' '.join(profname.split(", ")[::-1])
    GeorgiaTech.SearchProfessor(profname)
    if GeorgiaTech.SearchProfessor(profname) == False:
        return []
    tid = GeorgiaTech.GetProfessorDetail('tid')
    page = r.get('https://www.ratemyprofessors.com/ShowRatings.jsp?tid=' + str(tid))
    tree = html.fromstring(page.content)

    comments = tree.xpath('//p[@class="commentsParagraph"]/text()')

    for i in range(0, len(comments)-1):
        comments[i] = (comments[i])[23:-19]

    return comments


def getProfRatings(profname):
    profname = ' '.join(profname.split(", ")[::-1])
    GeorgiaTech.SearchProfessor(profname)
    if GeorgiaTech.SearchProfessor(profname) == 'error':
        return []
    tid = GeorgiaTech.GetProfessorDetail('tid')
    url = "https://www.ratemyprofessors.com/ShowRatings.jsp?tid=" + str(tid)

    page = r.get(url)
    tree = html.fromstring(page.content)
    ratings = tree.xpath('//div[@class="descriptor-container"]/span/text()')

    indexes = []
    updatedRatings = []

    x = 0
    for i in range(0, len(ratings)-1):
        if x < len(ratings) - 1:
            indexes.append(x)
        else:
            break
        x = x + 4

    for i in indexes:
        updatedRatings.append(float(ratings[i]))

    return updatedRatings

def exists(profname):
    profname = ' '.join(profname.split(", ")[::-1])
    if (GeorgiaTech.SearchProfessor(profname) == False):
        return False
    else:
        return True


'''
masterratings = []
mastercomments = []

with open('profs.txt', 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        masterratings.extend(getProfRatings(lines[0][:-1]))
        mastercomments.extend(getProfComments(lines[0][:-1]))


master = {'Comments': mastercomments,
          'Ratings': masterratings}

df = DataFrame(master, columns=['Comments', 'Ratings'])

print(df)

export_csv = df.to_csv(r""+cwd+"\\commentdata.csv", index=None, header=True)

fp.close()
'''