"""
Добавить в конец списка words строку в переменной new_word.

После обновления списка, вывести его на экран с помощью print.

Список words нельзя менять вручную, то есть нельзя дописывать слово
"result" в конце списка, надо поменять его с помощью Python.
"""

words = ["line", "test", "column"]
new_word = "result"
words.append(new_word)
print(words)
