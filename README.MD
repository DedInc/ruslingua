# RusLingua 📚

RusLingua is a Python library for retrieving various linguistic information about Russian words. It provides a simple API to get synonyms, antonyms, cognate words, and definitions.

## Features

- Get synonyms of a word 👥
- Get antonyms of a word 👎
- Get cognate words (words with a common root) 🌳
- Get definitions from dictionaries 📖

## Quickstart

### Synchronous Usage
```python
from ruslingua import RusLingua

ruslingua = RusLingua()

synonyms = ruslingua.get_synonyms('дом')
antonyms = ruslingua.get_antonyms('дом')
cognates = ruslingua.get_cognate_words('дом')
definition = ruslingua.get_definition('дом')

print(synonyms)
print(antonyms)
print(cognates)
print(definition)
```

### Asynchronous Usage
```python
import asyncio
from ruslingua import AsyncRusLingua

async def main():
    ruslingua = AsyncRusLingua()

    synonyms = await ruslingua.get_synonyms('дом')
    antonyms = await ruslingua.get_antonyms('дом')
    cognates = await ruslingua.get_cognate_words('дом')
    definition = await ruslingua.get_definition('дом')

    print(synonyms)
    print(antonyms)
    print(cognates)
    print(definition)

if __name__ == "__main__":
    asyncio.run(main())
```

## Installation 

```
pip install ruslingua
```

## Usage

### Synchronous

Import the `RusLingua` class and instantiate it:

```python
from ruslingua import RusLingua

ruslingua = RusLingua()
```

Then call the methods with a word to get the linguistic information:

```python
synonyms = ruslingua.get_synonyms('дом')
antonyms = ruslingua.get_antonyms('дом')
cognates = ruslingua.get_cognate_words('дом')
definition = ruslingua.get_definition('дом')
```

### Asynchronous

Import the `AsyncRusLingua` class and use it with `asyncio`:

```python
import asyncio
from ruslingua import AsyncRusLingua

async def main():
    ruslingua = AsyncRusLingua()
    # ... use the methods as shown in the quickstart ...

if __name__ == "__main__":
    asyncio.run(main())
```

The methods return lists of strings.

## Credits 

RusLingua retrieves data from various sources:

- [jeck.ru](https://jeck.ru) - synonyms 👥
- [razbiraem-slovo.ru](https://razbiraem-slovo.ru) - antonyms 👎 and cognate words 🌳
- [gramota.ru](https://gramota.ru) - definitions 📖
