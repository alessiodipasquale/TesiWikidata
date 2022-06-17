import json
from turtle import color
import matplotlib.pyplot as plt
import json
import numpy as np
import operator
names = {
    "Q27058":"Approximation",
    "Q41719":"Hypothesis",
    "Q11169":"Question Mark",
    "Q29485":"Error",
    "Q101244":"acronym",
    "Q102786":"abbreviation",
    "Q61002":"pseudonym",
    "Q357662":"work in process",
    "Q603908":"to be announced",
    "Q280943":"deprecation",
    "Q701040":"annulment",
    "Q873222":"expulsion",
    "Q880643":"false statement",
    "Q1255828":"controversy",
    "Q1309409":"unanimity",
    "Q3918409":"proposal",
    "Q13649246":"uncertainty",
    "Q17024293":"misunderstanding",
    "Q18603603":"hypothetically",
    "Q18122778":"presumably",
    "Q18912752":"disputed",
    "Q25895909":"cannot be confirmed by other sources",
    "Q24238356":"unknown",
    "Q24025284":"sometimes changes",
    "Q20734200":"not completed",
    "Q26932615":"statement with potentially incorrect Julian date",
    "Q28831311":"unconfirmed",
    "Q28962310":"rarely",
    "Q28962312":"often",
    "Q29023906":"temporary exhibition",
    "Q29509043":"official",
    "Q29509080":"unofficial",
    "Q30230067":"possibly",
    "Q30108381":"cancelled",
    "Q37113960":"estimate",
    "Q45025362":"replaced entity",
    "Q38131096":"rediscovery",
    "Q50376823":"expected",
    "Q56644435":"probably",
    "Q54943392":"obsolete form",
    "Q59864995":"optional",
    "Q73290844":"speculation",
    "Q74524855":"most frequent value",
    "Q84590041":"name change",
    "Q97161074":"Guesstimate",
    "Q100349848":"partially",
    "Q104378399":"dubious",
    "Q107217620":"unsubstantiated",
    "Q106466760":"manipulation",
    "Q107356532":"obsolete",
    "Q110143752":"sometimes",
    "Q110290991":"no earlier than",
    "Q108163":"proposition",
    "Q5727902":"circa",
    "Q4895105":"interim",
    "Q744069":"extrapolation",
    "Q748250":"prediction",
    "Q21818619":"near",
    "Q23013246":"copy",
    "Q6136054":"guess",
    "Q32188232":"allegedly"
}

with open('dataset2\countNatureResults.json','r') as file:
    data = json.load(file)
    count = []
    entity = []
    data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    print(data[0][1])

   # for key in data:
    #    if(key != 'unknown'):
     #       count.append(data[key])
      #      entity.append(key)
    for el in data:
        if (el[0] != 'unknown'):
            entity.append(names.get(el[0]))
            count.append(el[1])
    ind = np.arange(len(count))
    plt.figure()
    plt.bar(ind, count, tick_label = entity, width= 0.8, color='purple')
    plt.xticks(fontsize=4, rotation =90)
    plt.show()