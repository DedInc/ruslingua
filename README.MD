<h1 align="center">wikionary - Модуль для поиска Синонимов, Антонимов и т.д.</h1>

<br>

<h1 align="center"> -Как это работает?- </h1>

```python
import wikionary as w

w.getSynonims('привет') #Найти синонимы к слову привет
w.getAntonyms('привет') #Найти антонимы к слову привет
w.getPhraseologs('привет') #Найти фразеологизмы к слову привет
w.getHyperonims('привет') #Найти гиперонимы к слову привет
w.getAssociations('привет') #Найти ассоциации к слову привет
w.getRandomWord() #Найти случайное слово
```