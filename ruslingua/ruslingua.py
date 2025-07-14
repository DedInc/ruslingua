import aiohttp
import asyncio
from selectolax.parser import HTMLParser
from urllib.parse import unquote

class AsyncRusLingua:
    def __init__(self):
        self.user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')
        self.headers = {'User-Agent': self.user_agent}

    async def get_html_tree(self, url):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url) as response:
                return HTMLParser(await response.text())

    async def get_synonyms(self, word):
        synonyms = []
        tree = await self.get_html_tree(
            f'https://jeck.ru/tools/SynonymsDictionary/{word}')
        
        for node in tree.css('td a'):
            url = node.attributes['href']
            if '+' not in url:
                parts = url.split('Dictionary/')
                if len(parts) > 1:
                    synonyms.append(unquote(parts[1]))
        
        return synonyms

    async def get_antonyms(self, word):
        tree = await self.get_html_tree(f'https://razbiraem-slovo.ru/antonyms/{word}')
        elements = tree.css("a[href*='antonyms']:not([class])")

        antonyms = [element.text(strip=True) for element in elements if element.text(strip=True)]
        return antonyms

    async def get_cognate_words(self, word):
        tree = await self.get_html_tree(f'https://razbiraem-slovo.ru/odnokorennye/{word}')
        elements = tree.css("a[href*='po-sostavu'][class]")

        cognates = [element.attributes['href'].split('/')[-1] for element in elements if 'разбор' in element.text(strip=True)]
        return cognates

    async def get_definition(self, word):
        tree = await self.get_html_tree(
            f'https://gramota.ru/poisk?query={word}&mode=slovari&l=1&dicts[]=42')
        
        description_node = tree.css_first("div.description")
        if description_node:
            return description_node.text(strip=True)
        return ""

class RusLingua:
    def __init__(self):
        self._async_lingua = AsyncRusLingua()

    def get_synonyms(self, word):
        return asyncio.run(self._async_lingua.get_synonyms(word))

    def get_antonyms(self, word):
        return asyncio.run(self._async_lingua.get_antonyms(word))

    def get_cognate_words(self, word):
        return asyncio.run(self._async_lingua.get_cognate_words(word))

    def get_definition(self, word):
        return asyncio.run(self._async_lingua.get_definition(word))
