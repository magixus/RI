from recherche.RI_Methodes import  reverseFileConstructionMethods as ifcm
import math

def pertinentContainWord(freq,pertinent,w):
  ri = 0
  for doc in pertinent:
    if (w,doc) in freq:
      ri += 1
  return ri

def documentsContainWord(freq,w):
  index = ifcm.indexmot(freq,w)
  return list(index.keys())

def getDocScores(freq,query,pertinent):
  fquery = ifcm.generateFreqOfQuery(query)
  docList = {}
  R = len(pertinent)
  for d in pertinent:
    weightd = ifcm.indexdoc(freq,d)
    s = 0.0
    for w in fquery:
      ri = pertinentContainWord(freq,pertinent,w)
      ni = len(documentsContainWord(freq,w))
      s += ifcm.f(weightd,w) * math.log10(((ri + 0.5) / (R - ri + 0.5)) / ((ni - ri + 0.5) /(ifcm.N - ni - R + ri + 0.5)))
      r = math.log10(((ri + 0.5) / (R - ri + 0.5)) / ((ni - ri + 0.5) /(ifcm.N - ni - R + ri + 0.5)))
    score = s
    docList[d] = score
  return docList