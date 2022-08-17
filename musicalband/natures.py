from html import entities
from itertools import count
import json
import os
from json.decoder import JSONDecodeError
directory = './'
normalRankCount = 0
preferredRankCount = 0
deprecatedRankCount = 0
claimsTotalNumber = 0
totalStatements = 0

#f = open('G:/tipi.json')
#data = json.loads(f.read())    
noResponseCounter = 0

data = {
    "value": "Q27058", "label":"Approximation",
    "value":"Q41719","label":"Hypothesis",
    "value":"Q11169","label":"Question Mark",
    "value":"Q29485","label":"Error",
    "value":"Q101244","label":"acronym",
    "value":"Q102786","label":"abbreviation",
    "value":"Q61002","label":"pseudonym",
    "value":"Q357662","label":"work in process",
    "value":"Q603908","label":"to be announced",
    "value":"Q280943","label":"deprecation",
    "value":"Q701040","label":"annulment",
    "value":"Q873222","label":"expulsion",
    "value":"Q880643","label":"false statement",
    "value":"Q1255828","label":"controversy",
    "value":"Q1309409","label":"unanimity",
    "value":"Q3918409","label":"proposal",
    "value":"Q13649246","label":"uncertainty",
    "value":"Q17024293","label":"misunderstanding",
    "value":"Q18603603","label":"hypothetically",
    "value":"Q18122778","label":"presumably",
    "value":"Q18912752","label":"disputed",
    "value":"Q25895909","label":"cannot be confirmed by other sources",
    "value":"Q24238356","label":"unknown",
    "value":"Q24025284","label":"sometimes changes",
    "value":"Q20734200","label":"not completed",
    "value":"Q26932615","label":"statement with potentially incorrect Julian date",
    "value":"Q28831311","label":"unconfirmed",
    "value":"Q28962310","label":"rarely",
    "value":"Q28962312","label":"often",
    "value":"Q29023906","label":"temporary exhibition",
    "value":"Q29509043","label":"official",
    "value":"Q29509080","label":"unofficial",
    "value":"Q30230067","label":"possibly",
    "value":"Q30108381","label":"cancelled",
    "value":"Q37113960","label":"estimate",
    "value":"Q45025362","label":"replaced entity",
    "value":"Q38131096","label":"rediscovery",
    "value":"Q50376823","label":"expected",
    "value":"Q56644435","label":"probably",
    "value":"Q54943392","label":"obsolete form",
    "value":"Q59864995","label":"optional",
    "value":"Q73290844","label":"speculation",
    "value":"Q74524855","label":"most frequent value",
    "value":"Q84590041","label":"name change",
    "value":"Q97161074","label":"Guesstimate",
    "value":"Q100349848","label":"partially",
    "value":"Q104378399","label":"dubious",
    "value":"Q107217620","label":"unsubstantiated",
    "value":"Q106466760","label":"manipulation",
    "value":"Q107356532","label":"obsolete",
    "value":"Q110143752","label":"sometimes",
    "value":"Q110290991","label":"no earlier than",
    "value":"Q108163","label":"proposition",
    "value":"Q5727902","label":"circa",
    "value":"Q4895105","label":"interim",
    "value":"Q744069","label":"extrapolation",
    "value":"Q748250","label":"prediction",
    "value":"Q21818619","label":"near",
    "value":"Q23013246","label":"copy",
    "value":"Q6136054","label":"guess",
    "value":"Q32188232","label":"allegedly"
}

data = {
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

count = {
    "Q27058":0,
    "Q41719":0,
    "Q11169":0,
    "Q29485":0,
    "Q101244":0,
    "Q102786":0,
    "Q61002":0,
    "Q357662":0,
    "Q603908":0,
    "Q280943":0,
    "Q701040":0,
    "Q873222":0,
    "Q880643":0,
    "Q1255828":0,
    "Q1309409":0,
    "Q3918409":0,
    "Q13649246":0,
    "Q17024293":0,
    "Q18603603":0,
    "Q18122778":0,
    "Q18912752":0,
    "Q25895909":0,
    "Q24238356":0,
    "Q24025284":0,
    "Q20734200":0,
    "Q26932615":0,
    "Q28831311":0,
    "Q28962310":0,
    "Q28962312":0,
    "Q29023906":0,
    "Q29509043":0,
    "Q29509080":0,
    "Q30230067":0,
    "Q30108381":0,
    "Q37113960":0,
    "Q45025362":0,
    "Q38131096":0,
    "Q50376823":0,
    "Q56644435":0,
    "Q54943392":0,
    "Q59864995":0,
    "Q73290844":0,
    "Q74524855":0,
    "Q84590041":0,
    "Q97161074":0,
    "Q100349848":0,
    "Q104378399":0,
    "Q107217620":0,
    "Q106466760":0,
    "Q107356532":0,
    "Q110143752":0,
    "Q110290991":0,
    "Q108163":0,
    "Q5727902":0,
    "Q4895105":0,
    "Q744069":0,
    "Q748250":0,
    "Q21818619":0,
    "Q23013246":0,
    "Q6136054":0,
    "Q32188232":0,
    "unknown":0
}

for file in os.listdir("/home/admin/musicalband/data"):
    with open('/home/admin/musicalband/data/'+file,'r') as f:
        data = json.load(f)
        entities = data['entities']
        for key in entities:
            el = entities[key]
            for claimsId in el['claims']:
                statement = el['claims'][claimsId]
                for statementId in el['claims'][claimsId]:
                    qualifiers =el['claims'][claimsId]
                    element = qualifiers.pop()
                    if 'qualifiers' in element:
                        qualifier = element['qualifiers']
                        if 'P5102' in qualifier:
                            for element in qualifier['P5102']:
                                datavalue = element['datavalue']
                                if datavalue['value']['id'] in count.keys():
                                    toChange = {datavalue['value']['id']: count.get(datavalue['value']['id'])+1 }
                                else:
                                    toChange = {"unknown": count.get("unknown")+1 }
                                count.update(toChange)

with open('/home/admin/musicalband/natures.json','w') as outfile:
    outfile.write(json.dumps(count, indent = 4))