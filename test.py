from dicts import *


'''
from frozendict import frozendict

# Данные
qwerty = frozendict({
    49: "02", 33: "02", 50: "03", 34: "03", 51: "04", 8470: "04", 54: "05", 59: "05",
    53: "06", 37: "06", 54: "07", 58: "07", 55: "08", 63: "08", 56: "09", 42: "09",
    57: "10", 40: "10", 48: "11", 41: "11", 45: "12", 95: "12", 61: "13", 43: "13",
    1081: "16", 1094: "17", 1091: "18", 1082: "19", 1077: "20", 1085: "21", 1075: "22",
    1096: "23", 1097: "24", 1079: "25", 1093: "26", 1098: "27", 10: "28", 1092: "30",
    1099: "31", 1074: "32", 1072: "33", 1087: "34", 1088: "35", 1086: "36", 1083: "37",
    1076: "38", 1078: "39", 1101: "40", 1105: "41", 92: "43", 47: "43", 1103: "44",
    1095: "45", 1086: "46", 1084: "47", 1080: "48", 1090: "49", 1100: "50", 1073: "51",
    1102: "52", 46: "53", 44: "53", 32: "57"
})

# Преобразуем и выводим символы
symbols = [chr(key) for key in qwerty.keys()]
print(symbols)
print(ord("\\"))
'''

"""
def count_characters_in_file(file_path):
    char_count = {}  # создаём пустой словарь для хранения символов и их количества
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()  # читаем весь текст из файла
            for char in text:
                if char in char_count:
                    char_count[char] += 1  # увеличиваем счётчик для символа
                else:
                    char_count[char] = 1  # добавляем символ в словарь с начальным значением 1
    except FileNotFoundError:
        print("Файл не найден!")
    return char_count
result = count_characters_in_file('d:/Институт/PYTHON/Травов/voina-i-mir.txt')
print(result)
"""
"""
def read_large_file(file_path: str, chunk_size: int):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk
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

count_symb(read_large_file('d:/Институт/PYTHON/Травов/тест.txt', 1024))


key_stress_ant= dict.fromkeys(ant.values(),0)
key_stress_qwer= dict.fromkeys(qwerty.values(),0)

def key_stress_counter(key_stress:dict,stress_sumbol:dict,rascl:dict):
    for symb in stress_sumbol.keys():
        key_stress[rascl[symb]] += stress_sumbol[symb]
    return key_stress
print(key_stress_counter(key_stress_qwer, score_symb, qwerty))
print(key_stress_counter(key_stress_ant, score_symb, ant))
