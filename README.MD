<h1 align="center">wikionary - Модуль для поиска Синонимов, Антонимов и Фразеологизмов.</h1>

<br>

<h1 align="center"> -Как это работает?- </h1>

```python
import wikionary as w

hello = w.getSynonims('привет') #Найти синонимы к слову привет
hello = w.getAntonyms('привет') #Найти антонимы к слову привет
hello = w.getPhraseologs('привет') #Найти фразеологизмы к слову привет
```