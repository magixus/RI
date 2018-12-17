from recherche.RI_Methodes import inverseFileConstructionMethods as ifcm
import math

def scoreInnerProduct(freq,fquery,w):
    return sum([ifcm.f(fquery,w)*ifcm.f(freq,w) for w in fquery])

def scoreCoefDice(freq,fquery,words):
    up = 2*scoreInnerProduct(freq,fquery,words)
    # words = set([w for w in freq]+[w for w in fquery])
    down = sum([ifcm.f(fquery,w)*ifcm.f(fquery,w)+ifcm.f(freq,w)*ifcm.f(freq,w) for w in words])
    #print ("DICE DOWN")
    #print (down)
    return (up/down)

def scoreCosin(freq,fquery,words):
    up = scoreInnerProduct(freq,fquery,words)
    # words = set([w for w in freq] + [w for w in fquery])
    s1 = sum([ifcm.f(fquery,w)*ifcm.f(fquery,w) for w in words])
    s2 = sum([ifcm.f(freq,w)*ifcm.f(freq,w) for w in words])
    down = math.sqrt(s1*s2)
    return up/down

def scoreJaccard(freq,fquery,words):
    up = scoreInnerProduct(freq,fquery,words)
    # words = set([w for w in freq] + [w for w in fquery])
    down = sum([ifcm.f(fquery,w)*ifcm.f(fquery,w)+ifcm.f(freq,w)*ifcm.f(freq,w) for w in words]) - up
    return up / down


def getDocScores(freq,query, computeFunction=scoreInnerProduct):
    weights = ifcm.getWeights(freq)
    fquery = ifcm.generateFreqOfQuery(query)
    words = set([w for (w,d) in freq])
    docList = []
    for d in ifcm.docs:
        weightd = ifcm.indexdoc(weights,d)
        score = computeFunction(weightd,fquery,words)
        docList.append(score)
    # print(docList)
    return docList

"""
query = "domaine qui permet de faire la recherche"
print(getDocScores(ifcm.freq,query,computeFunction=scoreInnerProduct))
print(getDocScores(ifcm.freq,query,computeFunction=scoreCoefDice))
print(getDocScores(ifcm.freq,query,computeFunction=scoreCosin))
print(getDocScores(ifcm.freq,query,computeFunction=scoreJaccard))
"""
