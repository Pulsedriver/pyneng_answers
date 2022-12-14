"""
Запросить у пользователя ввод цвета через input.

Если введенный цвет есть в списке colors, вывести сообщение "Такой цвет есть".
Если цвета нет, вывести сообщение "В списке colors нет такого цвета".

Сделать так чтобы пользователь мог вводить цвет в любом регистре, но при этом
проверка для слова работала (ниже пример).

Пример работы задания:
$ python task_11.py
Введите цвет: red
Такой цвет есть

$ python task_11.py
Введите цвет: Red
Такой цвет есть

$ python task_11.py
Введите цвет: RED
Такой цвет есть

$ python task_11.py
Введите цвет: blue
В списке colors нет такого цвета

Для выполнения задания нельзя менять список colors.
"""
colors = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']

