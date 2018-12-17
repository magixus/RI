from recherche.RI_Methodes import reverseFileConstructionMethods as ifcm


def getFreq(reverseFile,w,d): # get frequence  of word  w in doc d
  if (w,d) in reverseFile:
    return reverseFile[w,d]
  return 0

def getIndex(index,key):
  if key in index:
    return index[key]
  return 0

def formatDocWeightsOutput(weights,reverseFile,word):
  output = []
  ws = ifcm.indexmot(weights,word)
  fs = ifcm.indexmot(reverseFile,word)
  for d in ifcm.docs:
    output.append([d,getIndex(fs,d),getIndex(ws,d)])
  return output

def formatWeightsPerDocOutput(weights,reverseFile,d):
  output = []
  ws = ifcm.indexdoc(weights,d)
  fs = ifcm.indexdoc(reverseFile,d)
  for w in fs.keys():
    output.append([w,getIndex(fs,w),getIndex(ws,w)])
  return output

