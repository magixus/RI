import basicMethods as bm
import math

def pertinentContainWord(freq,pertinent,w):
    ri = 0
    for doc in pertinent:
        if (w,doc) in freq:
            ri += 1
    print(w + " is in pertinent: " + str(ri))
    return ri

def documentsContainWord(freq,w):
    index = bm.indexmot(freq,w)
    print(w+" is in documents: " + str(len(index)))
    return len(index)

def getDocScores(freq,query,N,pertinent):
    # freq = bm.generateReversedFile(path,N)
    weights = bm.getWeights(freq,N)
    fquery = bm.generateFreqOfQuery(query)
    print(pertinent)
    docList = []
    R = len(pertinent)
    for d in range(1, N+1):
        weightd = bm.indexdoc(weights,d)
        print("for doc " + str(d))
        s = 0
        for w in fquery:
            ri = pertinentContainWord(freq,pertinent,w)
            ni = documentsContainWord(freq,w)
            s = s + (
                f(weightd,w)*math.log10(((ri + 0.5) / (R - ri + 0.5)) / ((ni - ri + 0.5) /
                                                            (N - ni - R + ri + 0.5))))
            r = math.log10(((ri + 0.5) / (R - ri + 0.5)) / ((ni - ri + 0.5) /
                                                            (N - ni - R + ri + 0.5)))
            print("result for %d %d is %f"%(ri,ni,r))
        score = s
        docList.append(score)
    # print(docList)
    return docList