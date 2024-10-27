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
    shift = 0
    for chunk in generator:
        for char in chunk:
            if char in alf:
                shift += 1
                char = char.lower()
            if ord(char) in score_symb:
                score_symb[ord(char)] += 1
    score_symb[0] += shift
    return(score_symb)
