from recherche.RI_Methodes import reverseFileConstructionMethods as ifcm


def getDocScores(freq,query):
  # freq = ifcm.generateReversedFile(path,N)
  stopWords = set(["and", "or", "(", ")", "not"])
  tab = set([w for w in query.split() if w not in stopWords])

  """
    when we give a request like "info and robotic" ==> 
    
  """
  docList = []
  for d in ifcm.docs:
    indexDoc = ifcm.indexdoc(freq, d) # frequence of all words in doc d
    newQuery = query
    for w in tab:
      if w in indexDoc.keys() :
        newQuery = newQuery.replace(w,"1")
      else:
        newQuery = newQuery.replace(w, "0")
    try:
      if (eval(newQuery)):
        docList.append(d)
    except Exception:
      print("wrong query format")
      break
  return docList
