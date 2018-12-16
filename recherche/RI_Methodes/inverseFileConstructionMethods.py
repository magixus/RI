from math import log10
from django.conf import settings
from os import listdir
from os.path import join
import re
import nltk

# get document root collections
mypath = join(settings.BASE_DIR, 'static/documents')

# get document number
N = len(listdir(mypath))


def f(freq,w):
  if w in freq:
    return freq[w]
  return 0

def fd(q,w,d):
  if w in q:
    return q[w,d]
  return 0

## load a file and return it content
def load(fileName):
  f = open(fileName, 'r', encoding="utf-8")
  str = f.read()
  f.close()
  return str

# separate stop items
listponctuation = set([".", ",", "!", "?","'","...",";","-"])
stopitem = set(load(join(mypath,"stopwords_fr.txt")).lower().split('\n')) | listponctuation


def generateReversedFile():
    freq = {}  # empty dict
    for f in listdir(mypath):
      ## get the text of the file and set it to lowercase
      if not f.startswith("stop"):
        text = load(join(mypath,f)).lower()
        # get all the words of the documents and filter stop items
        splitter = re.compile('\\W*')
        fd = nltk.FreqDist([s.lower() for s in splitter.split(text) if s not in stopitem])

        for w in fd.keys():
          freq[w, f] = fd[w]
    return freq

def generateFreqOfQuery(query):
    # get frequence of all usefull element from the query
    return nltk.FreqDist([w for w in query.lower().split() if w not in stopitem])

#Exercice 02
def indexdoc(freq,d): # freq of all words of doc d
  f = {}
  for(a,b) in freq:
    if b==d:
      f[a] = freq[a,b]
  return f

def indexmot(freq,w):  # freq of a given words in each doc
  f = {}
  for (a,b) in freq:
    if a==w:
      f[b] = freq[a,b]
  return f

def getNi(freq): # freq of all words in all docs
  ni = {}
  for (w,d) in freq:
    if not w in ni:
      ni[w] = 0
    ni[w] += 1
  return ni

def maxFreq(freq):
    maxF = {}
    for file in listdir(mypath):
      if not file.startswith("stop"):
        maxF[file] = max([freq[w,d] for (w,d) in freq if d==file])
    return maxF

def getWeights(freq):
    ni = getNi(freq)
    MAX = maxFreq(freq)
    poids = {}
    for (w, d) in freq:
        poids[w, d] = (float(freq[w, d]) / float(MAX[d])) * log10(float(N) / float(ni[w])+1)
    return poids



freq = generateReversedFile()
print(freq)
print(getWeights(freq))
print(maxFreq(freq))