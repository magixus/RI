from django.shortcuts import render
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
    return render(request, 'recherche/mydocuments.html', {'docs': file_list_title})


def statistics(request):
    Fil = load(join(mypath, listdir(mypath)[1])).split(' ')
    fd = nltk.FreqDist(Fil)
    wordscomm = list(fd.keys());
    wordscoust = list(fd.values());

    print(fd.keys())

    return render(request, 'recherche/statistics.html', {'wordscomm': wordscomm, 'wordscoust': wordscoust})


def infos(request):
    return render(request, 'recherche/about.html')


## load a file and return it content
def load(fileName):
    f = open(fileName, 'r', encoding="utf-8")
    str = f.read()
    f.close()
    return str


## show document content on the web
def show_doc(request, doc):
    file = doc + ".txt"
    doc_path = join(mypath, file)
    str_doc = load(doc_path)
    return HttpResponse(str_doc)


def searchTags(request):
    # récupération du mot

    # je fait une request é almaaany.com et je récupère les defs

    # je récupère la list des fichiers

    """
        t1 = f1
        rest = t1.concordance(" hadjer ")


    :param request:
    :return:
    """

    return render(request, "recherche/index.html")