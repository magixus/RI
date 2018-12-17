from recherche.RI_Methodes import ProbaModel
from recherche.RI_Methodes import VectorialModel
from recherche.RI_Methodes import inverseFileConstructionMethods as ifcm
from recherche.RI_Methodes.BooleanModel import getDocScores


def getFreq(inverseFile,w,d):
  if (w,d) in inverseFile:
    return inverseFile[w,d]
  return 0

def getIndex(index,key):
  if key in index:
    return index[key]
  return 0

def formatDocWeightsOutput(weights,inverseFile,word,N):
  output = []
  ws = ifcm.indexmot(weights,word)
  fs = ifcm.indexmot(inverseFile,word)
  print(ifcm.fd(weights, word, 3))
  print(fs)
  print(ws)
  for d in range(1,N+1):
    output.append([d,getIndex(fs,d),getIndex(ws,d)])
  return output

def formatWeightsPerDocOutput(weights,inverseFile,d,N):
  output = []
  ws = ifcm.indexdoc(weights,d)
  fs = ifcm.indexdoc(inverseFile,d)
  for w in fs.keys():
    output.append([w,getIndex(fs,w),getIndex(ws,w)])
  return output

def formatWeightsBoolean(inverseFile,query,N):
  output = []
  docs = getDocScores(inverseFile,query,N)
  for i,doc in enumerate(docs):
    if doc:
      output.append([i+1])
  if not len(output):
    output.append(["aucun document!"])
  return output

def formatWeightsVec(inverseFile,query,N,method):
  output = []
  docs = VectorialModel.getDocScores(inverseFile,query,N,method)
  docs = [(i, doc) for i, doc in enumerate(docs)]
  docs.sort(key=lambda x: x[1],reverse=True)
  for i,doc in docs:
    output.append([i+1,doc])
  return output

def formatWeightsProb(inverseFile,query,N,method):
  output = []
  docs = VectorialModel.getDocScores(inverseFile,query,N,method)
  docs = [(i,doc) for i,doc in enumerate(docs)]
  docs.sort(key=lambda x:x[1],reverse=True)
  #for i,doc in docs:
  # output.append([QtGui.QCheckBox("document non pertinent"),i+1,doc])
  return output

def formatWeightsProb2(inverseFile,query,N,pertinent):
  output = []
  docs = ProbaModel.getDocScores(inverseFile,query,N,pertinent)
  docs = [(i,doc) for i,doc in enumerate(docs)]
  docs.sort(key=lambda x:x[1],reverse=True)
  #for i,doc in docs:
  #  output.append([QtGui.QCheckBox("document non pertinent"),i+1,doc])
  return output

