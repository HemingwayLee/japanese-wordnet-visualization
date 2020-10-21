import json
import traceback
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .core import WordnetWrapper

wrapper = WordnetWrapper()

def index(request):
    return render(request, 'index.html')

def getTblCount(request, tbl):
    try:
        count = wrapper.getTblCount(tbl)
        return JsonResponse(count, safe=False, status=200)
    except Exception:
        print(traceback.format_exc())
        return JsonResponse({"msg": "Exception thrown"}, safe=False, status=500)

def getTblRows(request, tbl, limit, offset):
    try:
        rows = wrapper.getTblRows(tbl, limit, offset)
        return JsonResponse(json.dumps(rows), safe=False, status=200)
    except Exception:
        print(traceback.format_exc())
        return JsonResponse({"msg": "Exception thrown"}, safe=False, status=500)

def getWords(request, lemma):
    try:
        words = wrapper.getWords(lemma)
        return JsonResponse(words, safe=False, status=200)
    except Exception:
        print(traceback.format_exc())
        return JsonResponse({"msg": "Exception thrown"}, safe=False, status=500)

def getNetwork(request, lemma):
    try:
        words = wrapper.getWordSense(lemma)
        return JsonResponse(_translate(lemma, words), safe=False, status=200)
    except Exception:
        print(traceback.format_exc())
        return JsonResponse({"msg": "Exception thrown"}, safe=False, status=500)


def _translate(lemma, words):
    links = []
    nodes = [{"name": lemma}]
    for idx, ws in enumerate(words):
        nodes.append({"name": ws["synset"]})
        links.append({"source": 0, "target": idx+1, "weight": 1})
    
    res = { "nodes": nodes, "links": links }
    print(res)
    return res