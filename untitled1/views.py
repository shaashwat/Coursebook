from django.shortcuts import render
from untitled1 import courselist
from untitled1 import critique
from untitled1 import sarcasm
from untitled1 import ratemyprof
from untitled1 import overallscore
def index(request):
    ratemyprof.setupRMP()
    if request.method == "POST":
        course = request.POST.get("course", None)
        info = courselist.getCourseInfo(course)
        easyProfGpa = critique.getcoursecritique(course)
        profnames = easyProfGpa[2]
        profscores = easyProfGpa[4]
        profratings = sarcasm.getSentimentList(easyProfGpa[2])
        print(profratings)
        averageSentiment = str(sarcasm.getAverageSentiment(easyProfGpa[1]))
        score = overallscore.getOverallScore(course)
        return render(request, 'index.html', {"v": info + easyProfGpa[0] + " The average sentiment (1 is good 0 is bad) is " + averageSentiment,
                                              "b0": profnames[0],
                                              "r0": round(profratings[0], 2),
                                              "s0": profscores[0],
                                              "b1": profnames[1],
                                              "r1": round(profratings[1], 2),
                                              "s1": profscores[1],
                                              "b2": profnames[2],
                                              "r2": round(profratings[2], 2),
                                              "s2": profscores[2],
                                              "b3": profnames[3],
                                              "r3": round(profratings[3], 2),
                                              "s3": profscores[3],
                                              "diffinc": score[0],
                                              "diffval": score[1]
                                              })

    elif request.method == "GET":
        return render(request, 'normal.html')



    return render(request, 'normal.html')