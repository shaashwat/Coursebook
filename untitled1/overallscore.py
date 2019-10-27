from untitled1 import critique
from untitled1 import sarcasm

def getOverallScore(courseID):
    courseinfo = critique.getcoursecritique(courseID)

    profgpalist = courseinfo[3]
    avggpa = 0
    for gpa in profgpalist:
        avggpa += gpa
    avggpa /= len(profgpalist)
    print(avggpa)

    proflist = courseinfo[2]
    sentimentlist = sarcasm.getSentimentList(proflist)
    avgsent = 0
    counter = 0
    for sent in sentimentlist:
        if sent >= 0:
            avgsent += sent
            counter += 1
    if counter != 0:
        avgsent /= counter
    else:
        avgsent = -1.0
    print(avgsent)
    overall = int(avggpa * avgsent * 25)
    if (overall < 0):
        return ('There is not enough data to anaylze the difficulty. The course evaluation may not be accurate...'), -overall
    return '',overall

def getProfOverallScore(prof):
    courseinfo = critique.getcoursecritique(courseID)

    profgpalist = courseinfo[3]
    avggpa = 0
    for gpa in profgpalist:
        avggpa += gpa
    avggpa /= len(profgpalist)
    print(avggpa)

    proflist = courseinfo[2]
    sentimentlist = sarcasm.getSentimentList(proflist)
    avgsent = 0
    counter = 0
    for sent in sentimentlist:
        if sent >= 0:
            avgsent += sent
            counter += 1
    if counter != 0:
        avgsent /= counter
    else:
        avgsent = -1.0
    print(avgsent)
    overall = int(avggpa * avgsent * 25)
    if (overall < 0):
        return ('There is not enough data to anaylze the difficulty. The course evaluation may not be accurate...'), -overall
    return '',overall

#print(getOverallScore(input("What course would you like to evaluate? \n")))

