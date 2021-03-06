from recherche.RI_Methodes import reverseFileConstructionMethods as ifcm
import math

def scoreInnerProduct(reverseFile,fquery,w):
    return sum([ifcm.f(fquery,w)*ifcm.f(reverseFile,w) for w in fquery])

def scoreCoefDice(reverseFile,fquery,words):
    up = 2*scoreInnerProduct(reverseFile,fquery,words)
    # words = set([w for w in reverseFile]+[w for w in fquery])
    down = sum([ifcm.f(fquery,w)*ifcm.f(fquery,w)+ifcm.f(reverseFile,w)*ifcm.f(reverseFile,w) for w in words])
    #print ("DICE DOWN")
    #print (down)
    return (up/down)

def scoreCosin(reverseFile,fquery,words):
    up = scoreInnerProduct(reverseFile,fquery,words)
    # words = set([w for w in reverseFile] + [w for w in fquery])
    s1 = sum([ifcm.f(fquery,w)*ifcm.f(fquery,w) for w in words])
    s2 = sum([ifcm.f(reverseFile,w)*ifcm.f(reverseFile,w) for w in words])
    down = math.sqrt(s1*s2)
    return up/down

def scoreJaccard(reverseFile,fquery,words):
    up = scoreInnerProduct(reverseFile,fquery,words)
    # words = set([w for w in reverseFile] + [w for w in fquery])
    down = sum([ifcm.f(fquery,w)*ifcm.f(fquery,w)+ifcm.f(reverseFile,w)*ifcm.f(reverseFile,w) for w in words]) - up
    return up / down


def getDocScores(reverseFile,query, computeFunction=scoreInnerProduct):
    weights = ifcm.getWeights(reverseFile)
    fquery = ifcm.generateFreqOfQuery(query)
    words = set([w for (w,d) in reverseFile])
    docList = {}
    for d in ifcm.docs:
        weightd = ifcm.indexdoc(weights,d)
        score = computeFunction(weightd,fquery,words)
        docList[d] = (score)
    return docList
