import json
from django.http import HttpResponse, JsonResponse
from .core import WordnetWrapper

def get_words(request, lemma):
    try:
        wrapper = WordnetWrapper()
        words = wrapper.getWords(lemma)

        return JsonResponse(words, safe=False, status=200)
    except Exception as ex:
        print(ex)
        return HttpResponse(status=500)
