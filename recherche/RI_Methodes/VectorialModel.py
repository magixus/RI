import basicMethods as bm
import math

from basicMethods import fd, f


def scoreInnerProduct(freq,fquery,words):
    return sum([f(fquery,w)*f(freq,w) for w in fquery])

def scoreCoefDice(freq,fquery,words):
    up = 2*scoreInnerProduct(freq,fquery,words)
    # words = set([w for w in freq]+[w for w in fquery])
    down = sum([f(fquery,w)*f(fquery,w)+f(freq,w)*f(freq,w) for w in words])
    print ("DICE DOWN")
    print (down)
    return (up/down)

def scoreCosin(freq,fquery,words):
    up = scoreInnerProduct(freq,fquery,words)
    # words = set([w for w in freq] + [w for w in fquery])
    s1 = sum([f(fquery,w)*f(fquery,w) for w in words])
    s2 = sum([f(freq,w)*f(freq,w) for w in words])
    down = math.sqrt(s1*s2)
    return up/down

def scoreJaccard(freq,fquery,words):
    up = scoreInnerProduct(freq,fquery,words)
    # words = set([w for w in freq] + [w for w in fquery])
    down = sum([f(fquery,w)*f(fquery,w)+f(freq,w)*f(freq,w) for w in words]) - up
    return up / down


def getDocScores(freq,query,
                 N,computeFunction=scoreInnerProduct):
    # freq = bm.generateReversedFile(path,N)
    weights = bm.getWeights(freq,N)
    fquery = bm.generateFreqOfQuery(query)
    words = set([w for (w,d) in freq])
    docList = []
    for d in range(1, N+1):
        weightd = bm.indexdoc(weights,d)

        score = computeFunction(weightd,fquery,words)
        docList.append(score)
    # print(docList)
    return docList

# query = "domaine qui permet de faire la recherche"
# path = "Chek/D"
# N = 3
# print(getDocScores(query,path,N))
# print(getDocScores(query,path,N,computeFunction=scoreCoefDice))
# print(getDocScores(query,path,N,computeFunction=scoreCosin))
# print(getDocScores(query,path,N,computeFunction=scoreJaccard))

