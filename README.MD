<h1 align="center">wikionary - Модуль для поиска Синонимов, Антонимов и т.д.</h1>

<br>

<h1 align="center"> -Как это работает?- </h1>

```python
import wikionary as w

print(w.getSynonims('привет')) #Найти синонимы к слову привет
print(w.getAntonyms('привет')) #Найти антонимы к слову привет
print(w.getPhraseologs('привет')) #Найти фразеологизмы к слову привет
print(w.getHyperonims('привет')) #Найти гиперонимы к слову привет
print(w.getAssociations('привет')) #Найти ассоциации к слову привет
print(w.getRandomWord()) #Найти случайное слово

print(w.inflectWord('привет')) #Сделать разбор по падежам
```