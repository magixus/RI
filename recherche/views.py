from recherche.froms import   searchForm
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from os import listdir
from os.path import join
import nltk

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


def searchTags(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = searchForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
      # process the data in form.cleaned_data as required
      # ...
      # redirect to a new URL:
      print("valide\n", form.cleaned_data )
      return render(request,"recherche/search.html")
    else :
      print("pas valide")
      return render(request, "recherche/search.html")

  # if a GET (or any other method) we'll create a blank form
  else:
    return render(request, "recherche/search.html")