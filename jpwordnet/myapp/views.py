from django.http import HttpResponse

from .core import WordnetWrapper

def hello(request, lemma):
    try:
        print(lemma)
        wrapper = WordnetWrapper()
        words = wrapper.getWords(lemma)
        print(words)

        return HttpResponse(status=200)
    except Exception as ex:
        print(ex)
        return HttpResponse(status=500)
