import sys
import sqlite3
from collections import namedtuple

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Word = namedtuple('Word', 'wordid lang lemma pron pos')
Sense = namedtuple('Sense', 'synset wordid lang rank lexid freq src')

class WordnetWrapper:
    # Only query
    conn = sqlite3.connect("wnjpn.db", check_same_thread=False)
    conn.row_factory = dict_factory
    
    def getTblCount(self, tbl):
        cur = self.conn.execute('SELECT COUNT(*) AS count FROM {}'.format(tbl))
        row = cur.fetchone()
        return row

    def getTblRows(self, tbl, count, skip):
        cur = self.conn.execute("SELECT * FROM {} LIMIT {} OFFSET {}".format(tbl, count, skip))
        rows = cur.fetchall()
        return rows

    def getWords(self, lemma):
        cur = self.conn.execute("SELECT * FROM word WHERE lemma=?", (lemma,))
        rows = cur.fetchall()
        return rows

    def getWordWithSense(self, lemma, lang='jpn'):
        cur = self.conn.execute("SELECT w.lemma, s.synset FROM word AS w INNER JOIN sense AS s ON w.wordid = s.wordid WHERE w.lemma=? AND w.lang=?", (lemma, lang))
        rows = cur.fetchall()
        print(rows)
        return rows

    def getSenseWithWord(self, synset, lemma, lang='jpn'):
        cur = self.conn.execute("SELECT w.lemma, s.synset FROM word AS w INNER JOIN sense AS s ON w.wordid = s.wordid WHERE s.synset=? AND w.lemma!=? AND w.lang=?", (synset,lemma, lang))
        rows = cur.fetchall()
        print(rows)
        return rows
    
    def getSenses(self, wid, lang='jpn'):
        senses = []
        cur = self.conn.execute("SELECT * FROM sense WHERE wordid=? and lang=?", (wid, lang))
        row = cur.fetchone()
        while row:
            senses.append(Sense(*row))
            row = cur.fetchone()
        return senses

    # def getSense(synset, lang='jpn'):
    #     cur = conn.execute("SELECT * FROM sense WHERE synset=? and lang=?",
    #         (synset,lang))
    #     row = cur.fetchone()
    #     if row:
    #         return Sense(*row)
    #     else:
    #         return None

    # Synset = namedtuple('Synset', 'synset pos name src')

    # def getSynset(synset):
    #     cur = conn.execute("SELECT * FROM synset WHERE synset=?", (synset,))
    #     row = cur.fetchone()
    #     if row:
    #         return Synset(*row)
    #     else:
    #         return None

    # SynLink = namedtuple('SynLink', 'synset1 synset2 link src')

    # def getSynLinks(sense, link):
    #     synLinks = []
    #     cur = conn.execute("SELECT * FROM synlink WHERE synset1=? and link=?", (sense.synset, link))
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
