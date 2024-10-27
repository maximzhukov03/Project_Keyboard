from dicts import *

"""
Генераторная функция, обрабатывающая текст по кускам 
"""

def read_large_file(file_path: str, chunk_size: int):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

"""
Функция подсчёта символов 
На вход получает генератор, обрабатывающий файл и возвращяет словарь вида | символ : количество |
"""

def count_symb(generator):
    for chunk in generator:
        for char in chunk:
            if ord(char) in score_symb:
                score_symb[ord(char)] += 1
    return(score_symb)
#count_symb(read_large_file('voina-i-mir.txt', 1024))

"""
Функция по посчёту SHIFT 
"""

def shift_checker(a: str):
    global shift
    shift = shift+1
    return ord(a.lower())

'''
def shift_count(score_symb: dict):
    shift_count_qwerty = 0
    shift_count_ant = 0
    for key in score_symb:
        if key in shift_qwerty:
            shift_count_qwerty += score_symb[key]
'''
count_symb(read_large_file('d:/Институт/PYTHON/Травов/тест.txt', 1024))
shift_count_qwerty = 0
shift_count_ant = 0
for key in score_symb:
    if key in shift_qwerty:
        shift_count_qwerty += score_symb[key]
print(score_symb)
print(shift_count_qwerty)

def finger_count()