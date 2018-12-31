import sys
import sqlite3
from collections import namedtuple

Word = namedtuple('Word', 'wordid lang lemma pron pos')
Sense = namedtuple('Sense', 'synset wordid lang rank lexid freq src')

class WordnetWrapper:
    # Only query
    conn = sqlite3.connect("wnjpn.db", check_same_thread=False)
    
    def getWords(self, lemma):
        words = []
        cur = self.conn.execute("select * from word where lemma=?", (lemma,))
        row = cur.fetchone()
        while row:
            words.append(Word(*row))
            row = cur.fetchone()
        return words

    # def getWord(wordid):
    #     cur = conn.execute("select * from word where wordid=?", (wordid,))
    #     return Word(*cur.fetchone())
    
    def getSenses(self, wid, lang='jpn'):
        senses = []
        cur = self.conn.execute("select * from sense where wordid=? and lang=?", (wid, lang))
        row = cur.fetchone()
        while row:
            senses.append(Sense(*row))
            row = cur.fetchone()
        return senses

    # def getSense(synset, lang='jpn'):
    #     cur = conn.execute("select * from sense where synset=? and lang=?",
    #         (synset,lang))
    #     row = cur.fetchone()
    #     if row:
    #         return Sense(*row)
    #     else:
    #         return None

    # Synset = namedtuple('Synset', 'synset pos name src')

    # def getSynset(synset):
    #     cur = conn.execute("select * from synset where synset=?", (synset,))
    #     row = cur.fetchone()
    #     if row:
    #         return Synset(*row)
    #     else:
    #         return None

    # SynLink = namedtuple('SynLink', 'synset1 synset2 link src')

    # def getSynLinks(sense, link):
    #     synLinks = []
    #     cur = conn.execute("select * from synlink where synset1=? and link=?", (sense.synset, link))
    #     row = cur.fetchone()
    #     while row:
    #         synLinks.append(SynLink(*row))
    #         row = cur.fetchone()
    #     return synLinks

    # def getSynLinksRecursive(senses, link, lang='jpn', _depth=0):
    #     for sense in senses:
    #         synLinks = getSynLinks(sense, link)
    #         if synLinks:
    #         print '  '*_depth + getWord(sense.wordid).lemma, getSynset(sense.synset).name
    #         _senses = []
    #         for synLink in synLinks:
    #         sense = getSense(synLink.synset2, lang)
    #         if sense:
    #             _senses.append(sense)
    #         getSynLinksRecursive(_senses, link, lang, _depth+1)
