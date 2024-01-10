import requests
from lxml import html
from urllib.parse import unquote

class RusLingua:
    def __init__(self):
        self.user_agent = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
        self.headers = {'User-Agent': self.user_agent}

    def get_html_tree(self, url):
        response = requests.get(url, headers=self.headers)
        return html.fromstring(response.content)

    def get_synonyms(self, word):
        synonyms = []
        tree = self.get_html_tree(
            f'https://jeck.ru/tools/SynonymsDictionary/{word}')
        
        for url in tree.xpath('//td/a/@href'):
            if '+' not in url:
                parts = url.split('Dictionary/')
                if len(parts) > 1:
                    synonyms.append(unquote(parts[1]))
        
        return synonyms

    def get_antonyms(self, word):
        tree = self.get_html_tree(f'https://razbiraem-slovo.ru/antonyms/{word}')
        elements = tree.xpath("//*[contains(@href, 'antonyms')][count(@class)=0]")

        antonyms = [element.text.strip() for element in elements if element.text.strip()]
        return antonyms

    def get_cognate_words(self, word):
        tree = self.get_html_tree(f'https://razbiraem-slovo.ru/odnokorennye/{word}')
        elements = tree.xpath("//*[contains(@href, 'po-sostavu')][count(@class)=1]")

        cognates = [element.attrib['href'].split('/')[-1] for element in elements if 'разбор' in element.text]
        return cognates

    def get_associations(self, word):
        associations = []
        tree = self.get_html_tree(
            f'https://wordassociations.net/ru/ассоциации-к-слову/{word}')
        
        for url in tree.xpath('//li/a/@href'):
            if 'D1%83/' in url:
                associations.append(unquote(url.split('D1%83/')[1]).lower())
        
        return associations

    def get_definition(self, word):
        tree = self.get_html_tree(
            f'https://gramota.ru/poisk?query={word}&mode=slovari&l=1&dicts[]=42')
        
        full_text = ''.join(tree.xpath("//div[contains(@class, 'description')]//text()"))
        
        return full_text.strip()