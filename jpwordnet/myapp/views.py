import os
import json
import traceback
from django.shortcuts import render
from dotenv import load_dotenv
from django.http import HttpResponse, JsonResponse
from .core import WordnetWrapper

wrapper = WordnetWrapper()

def index(request):
    load_dotenv("./jpwordnet/.env")
    return render(request, 'index.html', {
        "WEBAPP_ADDRESS": os.environ.get("WEBAPP_ADDRESS")
    })

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
        words = wrapper.getWordWithSense(lemma)
        return JsonResponse(_translate(lemma, words), safe=False, status=200)
    except Exception:
        print(traceback.format_exc())
        return JsonResponse({"msg": "Exception thrown"}, safe=False, status=500)


def _translate(lemma, words):
    links = []
    nodes = [{"name": lemma, "color": "red"}]
    idx = 1
    for ws in words:
        currIdx = idx

        nodes.append({"name": ws["synset"], "color": "blue"})
        links.append({"source": 0, "target": idx, "weight": 1})
        newWords = wrapper.getSenseWithWord(ws["synset"], lemma)
        idx = idx + 1
        for nws in newWords:
            nodes.append({"name": nws["lemma"], "color": "red"})
            links.append({"source": currIdx, "target": idx, "weight": 1})
            idx = idx + 1
    
    res = { "nodes": nodes, "links": links }
    print(res)
    return res
