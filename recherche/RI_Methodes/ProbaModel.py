from recherche.RI_Methodes import  inverseFileConstructionMethods as ifcm
import math

def pertinentContainWord(freq,pertinent,w):
  ri = 0
  for doc in pertinent:
    if (w,doc) in freq:
      ri += 1
  print(w + " is in pertinent: " + str(ri))
  return ri

def documentsContainWord(freq,w):
  index = ifcm.indexmot(freq,w)
  print(w+" is in %d documents: " % str(len(index)))
  return len(index)

def getDocScores(freq,query,pertinent):
  # freq = ifcm.generateReversedFile(path,N)
  weights = ifcm.getWeights(freq)
  fquery = ifcm.generateFreqOfQuery(query)
  docList = []
  R = len(pertinent)
  for d in ifcm.docs:
    weightd = ifcm.indexdoc(weights,d)
    s = 0
    for w in fquery:
      ri = pertinentContainWord(freq,pertinent,w)
      ni = documentsContainWord(freq,w)
      s = s + (f(weightd,w)*math.log10(((ri + 0.5) / (R - ri + 0.5)) / ((ni - ri + 0.5) /(N - ni - R + ri + 0.5))))
      r = math.log10(((ri + 0.5) / (R - ri + 0.5)) / ((ni - ri + 0.5) /(N - ni - R + ri + 0.5)))
    score = s
    docList.append(score)
  # print(docList)
  return docList