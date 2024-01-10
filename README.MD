# RusLingua 📚

RusLingua is a Python library for retrieving various linguistic information about Russian words. It provides a simple API to get synonyms, antonyms, word associations, cognate words, and definitions.

## Features

- Get synonyms of a word 👥
- Get antonyms of a word 👎
- Get word associations 💭
- Get cognate words (words with a common root) 🌳
- Get definitions from dictionaries 📖

## Quickstart

```python
from ruslingua import RusLingua

ruslingua = RusLingua()

synonyms = ruslingua.get_synonyms('дом')
antonyms = ruslingua.get_antonyms('дом')
associations = ruslingua.get_associations('дом')
cognates = ruslingua.get_cognate_words('дом')  
definition = ruslingua.get_definition('дом')

print(synonyms)  
print(antonyms)
print(associations)
print(cognates)
print(definition)
```

## Installation 

```
pip install ruslingua
```

## Usage

Import the RusLingua class and instantiate it:

```python
from ruslingua import RusLingua

ruslingua = RusLingua()
```

Then call the methods with a word to get the linguistic information:

```python 
synonyms = ruslingua.get_synonyms('дом')
antonyms = ruslingua.get_antonyms('дом')
associations = ruslingua.get_associations('дом')
cognates = ruslingua.get_cognate_words('дом')
definition = ruslingua.get_definition('дом') 
```

The methods return lists of strings.

## Credits 

RusLingua retrieves data from various sources:

- [jeck.ru](https://jeck.ru) - synonyms 👥
- [razbiraem-slovo.ru](https://razbiraem-slovo.ru) - antonyms 👎 and cognate words 🌳
- [wordassociations.net](https://wordassociations.net) - word associations 💭
- [gramota.ru](https://gramota.ru) - definitions 📖