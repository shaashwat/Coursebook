from django.shortcuts import render
from untitled1 import courselist
from untitled1 import critique
from untitled1 import sarcasm
from untitled1 import ratemyprof
from untitled1 import overallscore
import csv
def index(request):
    ratemyprof.setupRMP()
    if request.method == "POST":
        course = request.POST.get("course", None).upper()
        courseexists = False
        with open('C:\\Users\\shaash\\PycharmProjects\\untitled1\\untitled1\\data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                if (course in row):
                    courseexists = True
                    break
        if not courseexists:
            return render(request, 'HomePage.html', {'p': "The input isn't valid. Try Again."})
        info = courselist.getCourseInfo(course)
        easyProfGpa = critique.getcoursecritique(course)
        profnames = easyProfGpa[2]
        profscores = easyProfGpa[4]
        profratings = sarcasm.getSentimentList(easyProfGpa[2])
        print(profratings)
        averageSentiment = str(sarcasm.getAverageSentiment(easyProfGpa[1]))
        score = overallscore.getOverallScore(course)
        gradedist = easyProfGpa[6]
        return render(request, 'CoursePage.html', {"v": "This course is " + info[0] + " which is " + info[1] + " credit hours.",
                                                   "b0": profnames[0],
                                                   "r0": round(profratings[0], 2),
                                                   "s0": profscores[0],
                                                   "g0": easyProfGpa[3][0],
                                                   "b1": profnames[1],
                                                   "r1": round(profratings[1], 2),
                                                   "s1": profscores[1],
                                                   "g1": easyProfGpa[3][1],
                                                   "b2": profnames[2],
                                                   "r2": round(profratings[2], 2),
                                                   "s2": profscores[2],
                                                   "g2": easyProfGpa[3][2],
                                                   "b3": profnames[3],
                                                   "r3": round(profratings[3], 2),
                                                   "s3": profscores[3],
                                                   "g3": easyProfGpa[3][3],
                                                   "diffval": score[1],
                                                   "avgGPA": round(easyProfGpa[5], 2),
                                                   "credits": info[1],
                                                   "course": info[0],
                                                   "ap0": gradedist[0][0],
                                                   "ap1": gradedist[0][1],
                                                   "ap2": gradedist[0][2],
                                                   "ap3": gradedist[0][3],
                                                   "bp0": gradedist[1][0],
                                                   "bp1": gradedist[1][1],
                                                   "bp2": gradedist[1][2],
                                                   "bp3": gradedist[1][3],
                                                   "cp0": gradedist[2][0],
                                                   "cp1": gradedist[2][1],
                                                   "cp2": gradedist[2][2],
                                                   "cp3": gradedist[2][3],
                                                   "dp0": gradedist[3][0],
                                                   "dp1": gradedist[3][1],
                                                   "dp2": gradedist[3][2],
                                                   "dp3": gradedist[3][3],
                                                   "fp0": gradedist[4][0],
                                                   "fp1": gradedist[4][1],
                                                   "fp2": gradedist[4][2],
                                                   "fp3": gradedist[4][3],
                                                   "wp0": gradedist[5][0],
                                                   "wp1": gradedist[5][1],
                                                   "wp2": gradedist[5][2],
                                                   "wp3": gradedist[5][3],
                                              })

    elif request.method == "GET":
        return render(request, 'HomePage.html', {'p': ""})



    return render(request, 'HomePage.html')