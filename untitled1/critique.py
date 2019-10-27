from lxml import html
import requests as r
from pandas import DataFrame
from untitled1 import ratemyprof
from untitled1.sarcasm import getAverageSentiment

'''
returns DataFrame type with all of the professor's names and information found on critique.gatech.edu
'''

def getcoursecritique(course):
    course = course.replace(' ', '')
    course = course.upper()
    page = r.get("https://critique.gatech.edu/course.php?id=" + course)
    tree = html.fromstring(page.content)
    prof_names = tree.xpath('//tr/td/a/text()')
    master = tree.xpath("//tr//td/text()")
    master = master[6:]
    prof_gpa = []
    prof_a = []
    prof_b = []
    prof_c = []
    prof_d = []
    prof_f = []
    prof_w = []
    exists_on_rmp = []
    prof_score = []
    for i in range(len(prof_names)):
        prof_gpa.append(float(master[(i) * 8 + 1]))
        prof_a.append(float(master[(i) * 8 + 2]))
        prof_b.append(float(master[(i) * 8 + 3]))
        prof_c.append(float(master[(i) * 8 + 4]))
        prof_d.append(float(master[(i) * 8 + 5]))
        prof_f.append(float(master[(i) * 8 + 6]))
        prof_w.append(float(master[(i) * 8 + 7]))
        exists_on_rmp.append(ratemyprof.exists(prof_names[i]))
        sentiment = getAverageSentiment(prof_names[i])
        if sentiment < 0:
            prof_score.append(None)
        else:
            prof_score.append(int(prof_gpa[i] * getAverageSentiment(prof_names[i]) * 25))

    prof = {'ProfessorName': prof_names,
            'AverageGPA': prof_gpa,
            'PercentA': prof_a,
            'PercentB': prof_b,
            'PercentC': prof_c,
            'PercentD': prof_d,
            'PercentF': prof_f,
            'PercentW': prof_w,
            'ExistsOnRMP': exists_on_rmp,
            'Score': prof_score}
    df = DataFrame(prof,
                   columns=['ProfessorName', 'AverageGPA', 'PercentA', 'PercentB', 'PercentC', 'PercentD', 'PercentF',
                            'PercentW', 'ExistsOnRMP', 'Score'])
    sorted_df = df.sort_values("ExistsOnRMP", ascending=False)
    profs = sorted_df.set_index("ProfessorName").T.to_dict('list')
    gpas = sorted_df.set_index("AverageGPA").T.to_dict('list')
    scores = sorted_df.set_index("Score").T.to_dict('list')
    scorelist = list(scores.keys())
    profname = next(iter(profs))
    formatted_name = " ".join(profname.split(", ")[::-1])
    proflist = list(profs.keys())
    if len(proflist)< 5:
        while len(proflist) < 5:
            proflist.append("")

    gpalist = list(gpas.keys())



    return (" " + formatted_name + " is the professor who's class had the highest average GPA, which was " + str(next(iter(gpas)))), profname, proflist[0:4], gpalist[0:4], scorelist[0:4], sum(gpalist)/len(gpalist)