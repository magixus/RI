import basicMethods as bm


def getDocScores(freq,query,N):
    # freq = bm.generateReversedFile(path,N)


    tab = query.split()
    stopWords = ['and', 'or', '(', ')', 'not']

    docList = []
    for d in range(1, N+1):
        indexDoc = bm.indexdoc(freq, d)
        newQuery = ""
        for w in tab:
            toAdd = w
            # print(w + " is in " + str(stopWords))
            # print(not(w in stopWords))
            if not (w in stopWords):
                if w in indexDoc.keys() and indexDoc[w] > 0:
                    toAdd = "1"
                else:
                    toAdd = "0"
            newQuery += toAdd + " "
        try:
            docList.append(eval(newQuery))
        except Exception:
            print("wrong query format")
            break

    # print(docList)
    return docList
