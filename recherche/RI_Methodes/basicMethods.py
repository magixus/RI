from math import log10
from django.conf import settings
from os import listdir
from os.path import join
import nltk


# get document root collections
mypath = join(settings.BASE_DIR, 'static/documents')
#get document number
N = len(listdir(mypath))

listcar = {'.', ',', '!', '?',"'","...",";","-"}
stoplist = open(join(mypath,"stopwords_fr.txt"), 'r').read().lower().split()


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

def generateReversedFile():
    k = 1
    freq = {}  # dict vide

    while k <= N:
        f = open(path + str(k) + '.txt', 'r')
        t = f.read()
        t = t.lower()
        i = 0
        while i < len(t):
            if t[i] in listcar:
                t = t.replace(t[i], " ")
            i += 1
        a = t.split()
        for w in a:
            if w not in stoplist and len(w) > 1:
                if (w, k) not in freq:
                    freq[w, k] = a.count(w)
                    # print(w, freq[w, k])
        k += 1
        f.close()
    # print("Le fichier inverse de la collection ")
    # for word in freq:
    #     print(word)
    return freq

def generateFreqOfQuery(query):
    query = query.lower()
    import re
    a = re.split('\s+',query)
    i = 0
    while i < len(query):
        if query[i] in listcar:
            query = query.replace(query[i], " ")
        i += 1

    f = {}
    for w in a:
        if w not in stoplist and len(w) > 1:
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

