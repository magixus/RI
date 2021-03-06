from recherche.froms import   searchForm, evaluteForm
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from os import listdir
from os.path import join
import nltk
from recherche.RI_Methodes import reverseFileConstructionMethods as RF
from recherche.RI_Methodes import BooleanModel as BM
from recherche.RI_Methodes import VectorialModel as VM
from recherche.RI_Methodes import ProbaModel as PM

# get reversefile
reversefile = RF.reverseFile


mypath = join(settings.BASE_DIR, 'static/documents')  # insert the path to our directory


def index(request):
  return render(request, "recherche/index.html")


def documents(request):
  # get files lis
  file_list = listdir(mypath)
  file_list_title = [l.split('.')[0] for l in file_list]
  # file_list_links = [mypath.join(l) for l in file_list]
  # render this list to view
  return render(request, 'recherche/search.html', {'docs': file_list_title})


def statistics(request):
  Fil = load(join(mypath, listdir(mypath)[0])).split(' ')
  fd = nltk.FreqDist(Fil)
  wordscomm = list(fd.keys())
  wordscoust = list(fd.values())

  print(wordscoust)

  return render(request, 'recherche/statistics.html', {'wordscomm': wordscomm, 'wordscoust': wordscoust})


def infos(request):
  return render(request, 'recherche/about.html')


## load a file and return it content
def load(fileName):
  f = open(fileName, 'r', encoding="utf-8")
  str = f.read()
  print(str)
  f.close()
  return str


## show document content on the web
def show_doc(request, doc):
  file = doc + ".txt"
  doc_path = join(mypath, file)
  str_doc = load(doc_path)
  return HttpResponse(str_doc)

m = ""
q = ""
def searchTags(request):
  global m
  global q
  res = set()
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = searchForm(request.POST)
    form_evaluate = evaluteForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
      q = query = form.cleaned_data['requete']
      mthod = form.cleaned_data['method']
      if not mthod.startswith("boo"):
        m = form.cleaned_data['appariement']

      if mthod.startswith('bool') :
        docs = BM.getDocScores(reversefile,query)
        return render(request, "recherche/search.html", {'b_documents':docs})

      else :
        if m.startswith("prod"):
          res = VM.getDocScores(reversefile,query,VM.scoreInnerProduct)
        elif m.startswith("coef"):
          res = VM.getDocScores(reversefile,query,VM.scoreCoefDice)
        elif m.startswith("cosinus"):
          res = VM.getDocScores(reversefile,query,VM.scoreCosin)
        elif m.startswith("jacc"):
          res = VM.getDocScores(reversefile,query,VM.scoreJaccard)

        if mthod.startswith("vect") : # request vect model
          return render(request, "recherche/search.html", {'v_documents':res})
        else: # reqest proba model
          return render(request, "recherche/search.html", {'p_documents':res})

    else :
      docsss = request.POST.getlist('pertinent[]')
      print(m)
      print(docsss)
      if m.startswith("prod"):
        res = PM.getDocScores(reversefile, q, docsss)
      elif m.startswith("coef"):
        res = PM.getDocScores(reversefile, q, docsss)
      elif m.startswith("cosinus"):
        res = PM.getDocScores(reversefile, q, docsss)
      elif m.startswith("jacc"):
        res = PM.getDocScores(reversefile, q, docsss)
      print(res)
      return render(request, "recherche/search.html",{'eval_prob':res})

  # if a GET (or any other method) we'll create a blank form
  else:
    return render(request, "recherche/search.html")
