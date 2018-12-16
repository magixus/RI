from PyQt4 import QtGui

import ProbaModel
import VectorialModel
import basicMethods as bm
from BooleanModel import getDocScores


def getFreq(freqs,w,d):
    if (w,d) in freqs:
        return freqs[w,d]
    return 0

def getIndex(index,key):
    if key in index:
        return index[key]
    return 0

def formatDocWeightsOutput(weights,freqs,word,N):
    output = []
    ws = bm.indexmot(weights,word)
    fs = bm.indexmot(freqs,word)
    print(bm.fd(weights, word, 3))
    print(fs)
    print(ws)
    for d in range(1,N+1):
        output.append([d,getIndex(fs,d),getIndex(ws,d)])
    return output

def formatWeightsPerDocOutput(weights,freqs,d,N):
    output = []
    ws = bm.indexdoc(weights,d)
    fs = bm.indexdoc(freqs,d)
    for w in fs.keys():
        output.append([w,getIndex(fs,w),getIndex(ws,w)])
    return output

def formatWeightsBoolean(freqs,query,N):
    output = []
    docs = getDocScores(freqs,query,N)
    for i,doc in enumerate(docs):
        if doc:
            output.append([i+1])
    if not len(output):
        output.append(["aucun document!"])
    return output

def formatWeightsVec(freqs,query,N,method):
    output = []
    docs = VectorialModel.getDocScores(freqs,query,N,method)
    docs = [(i, doc) for i, doc in enumerate(docs)]
    docs.sort(key=lambda x: x[1],reverse=True)
    for i,doc in docs:
        output.append([i+1,doc])
    return output

def formatWeightsProb(freqs,query,N,method):
    output = []
    docs = VectorialModel.getDocScores(freqs,query,N,method)
    docs = [(i,doc) for i,doc in enumerate(docs)]
    docs.sort(key=lambda x:x[1],reverse=True)
    for i,doc in docs:
        output.append([QtGui.QCheckBox("document non pertinent"),i+1,doc])
    return output

def formatWeightsProb2(freqs,query,N,pertinent):
    output = []
    docs = ProbaModel.getDocScores(freqs,query,N,pertinent)
    docs = [(i,doc) for i,doc in enumerate(docs)]
    docs.sort(key=lambda x:x[1],reverse=True)
    for i,doc in docs:
        output.append([QtGui.QCheckBox("document non pertinent"),i+1,doc])
    return output

