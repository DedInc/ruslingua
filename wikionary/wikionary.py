from lxml import html, etree
from pymorphy2 import MorphAnalyzer
from requests import get
from urllib.parse import unquote

agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
headers = {'User-Agent': agent}

def getSynonims(word):
    syns = []
    tree = html.fromstring(get(
        'https://jeck.ru/tools/SynonymsDictionary/{}'.format(word), headers=headers).content)
    urls = tree.xpath('//td/a/@href')
    for url in urls:
        if not '+' in url:
            dem = url.split('Dictionary/')
            if len(dem) > 1:
                word = unquote(dem[1])
                syns.append(word)
    return syns


def getAntonyms(word):
    antonyms = []
    tree = html.fromstring(
        get('https://ru.wiktionary.org/wiki/{}'.format(word), headers=headers).content)
    for k in range(1, 100):
        for i in range(1, 100):
            try:
                anto = tree.xpath(
                    '/html/body/div[3]/div[3]/div[5]/div[1]/ol[3]/li[{}]/a[{}]/text()'.format(i, k))
                antonyms.append(anto[0])
            except:
                break
    return list(dict.fromkeys(antonyms))


def getPhraseologs(word):
    phraseols = []
    tree = html.fromstring(
        get('https://ru.wiktionary.org/wiki/{}'.format(word), headers=headers).content)
    for k in range(1, 100):
        for i in range(1, 100):
            try:
                phrase = tree.xpath(
                    '/html/body/div[3]/div[3]/div[5]/div[1]/ul[1]/li[{}]/a[{}]/text()'.format(k, i))
                if not 'МФА' in phrase:
                    phraseols.append(phrase[0])
            except:
                break
    return list(dict.fromkeys(phraseols))


def getRandomWord():
    tree = html.fromstring(
        get('https://ru.wiktionary.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0', headers=headers).content)
    return tree.xpath('/html/body/div[3]/h1/text()')[0]


def getAssociations(word):
    assocs = []
    tree = html.fromstring(get(
        'https://wordassociations.net/ru/%D0%B0%D1%81%D1%81%D0%BE%D1%86%D0%B8%D0%B0%D1%86%D0%B8%D0%B8-%D0%BA-%D1%81%D0%BB%D0%BE%D0%B2%D1%83/{}'.format(word), headers=headers).content)
    urls = tree.xpath('//li/a/@href')
    for url in urls:
        if 'D1%83/' in url:
            assocs.append(unquote(url.split('D1%83/')[1]).lower())
    return assocs


def getHyperonims(word):
    tree = html.fromstring(
        get('https://ru.wiktionary.org/wiki/{}'.format(word), headers=headers).content)
    phraseols = []
    for k in range(1, 100):
        for i in range(1, 100):
            try:
                phrase = tree.xpath(
                    '/html/body/div[3]/div[3]/div[5]/div[1]/ol[4]/li[{}]/a[{}]/text()'.format(k, i))
                phraseols.append(phrase[0])
            except:
                break
    return list(dict.fromkeys(phraseols))

def checkWord(diction, word):
    keys = list(diction.keys())
    for key in keys:
        if diction[key] == word:
            return True
    return False

def inflectWord(word):
    inflected = {}

    morph = MorphAnalyzer()
    p = morph.parse(word)[0]
    types = ('nomn', 'gent', 'datv', 'accs', 'ablt', 'loct', 'voct', 'gen2', 'acc2', 'loc2')
    for t in types:
        a = p.inflect({t})
        try:
            if not checkWord(inflected, a.word):
                inflected[t] = a.word
        except:
            return {}

    return inflected