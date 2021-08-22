from lxml import html
from requests import get


def getSynonims(word):
    tree = html.fromstring(
        get('https://ru.wiktionary.org/wiki/{}'.format(word)).content)
    syns = []
    for l in range(10):
        for k in range(10):
            for i in range(10):
                try:
                    syn = tree.xpath(
                        '/html/body/div[3]/div[3]/div[5]/div[1]/ol[2]/li[{}]/span[{}]/a[{}]/text()'.format(l, k, i))
                    syns.append(syn[0])
                except:
                    pass
    return list(dict.fromkeys(syns))


def getAntonyms(word):
    tree = html.fromstring(
        get('https://ru.wiktionary.org/wiki/{}'.format(word)).content)
    antonyms = []
    for i in range(10):
        try:
            anto = tree.xpath(
                '/html/body/div[3]/div[3]/div[5]/div[1]/ol[3]/li[1]/a[{}]/text()'.format(i))
            antonyms.append(anto[0])
        except:
            pass
    return list(dict.fromkeys(antonyms))


def getPhraseologs(word):
    tree = html.fromstring(
        get('https://ru.wiktionary.org/wiki/{}'.format(word)).content)
    phraseols = []
    for k in range(10):
        for i in range(10):
            try:
                phrase = tree.xpath(
                    '/html/body/div[3]/div[3]/div[5]/div[1]/ul[1]/li[{}]/a[{}]/text()'.format(k, i))
                phraseols.append(phrase[0])
            except:
                pass
    return list(dict.fromkeys(phraseols))
