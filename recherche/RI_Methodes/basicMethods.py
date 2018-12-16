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
        print(fd)

        for w in fd.keys():
          freq[w, f] = fd[w]
    return freq

def generateFreqOfQuery(query):
    query = query.lower()
    a = re.split('\s+',query)
    i = 0
    while i < len(query):
        if query[i] in listcar:
            query = query.replace(query[i], " ")
        i += 1

    f = {}
    for w in a:
        if w not in stopitem and len(w) > 1:
            if w not in f:
                f[w] = a.count(w)

    return f

#Exercice 02
def indexdoc(freq,d): #fonction pr 1 document
    # print("l'index du Document ",d," est")
    f = {}
    for(a,b) in freq:
        if b==d:
            f[a] = freq[a,b]
    return f

def indexmot(freq,w):  #fonction pr 1 mot
    # print("l'index du mot ",w," est")
    f = {}
    for (a,b) in freq:
        if a==w:
            f[b] = freq[a,b]

    return f

def getNi(freq):
    ni = {}
    for (w,d) in freq:
        if not w in ni:
            ni[w] = 0
        ni[w] += 1
    return ni

def maxFreq(freq,N):
    maxF = {}
    for doc in range(1,N+1):
        maxF[doc] = max([freq[w,d] for (w,d) in freq if d==doc])
    return maxF

def getWeights(freq,N):
    ni = getNi(freq)
    maxes = maxFreq(freq,N)
    poids = {}
    for (w, d) in freq:
        poids[w, d] = (float(freq[w, d]) / float(maxes[d])) * log10(float(N) / float(ni[w])+1)
    return poids



freq = generateReversedFile()

print(freq)