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
            if char in alfset:
                shift += 1
                char = char.lower()
            if ord(char) in score_symb:
                score_symb[ord(char)] += 1
    score_symb[0] += shift
    return(score_symb)

"""
Подсчёт шифтов для уникальных символов 
"""

def dop_shift(set_shift:set,symbol_strees:dict):
    shift=0
    for sym in set_shift:
        shift+=symbol_strees[sym]
    return shift

key_stress_ant= dict.fromkeys(ant.values(),0)
key_stress_qwer= dict.fromkeys(qwerty.values(),0)

def key_stress_counter(key_stress:dict,stress_sumbol:dict,rascl:dict,shift:int):
    for symb in stress_sumbol.keys():
        key_stress[rascl[symb]]+=stress_sumbol[symb]
    key_stress["42"]+=shift
    return key_stress 

def finger_stress_counter(fin_count:dict,key_stress:dict,main_dict:frozendict):
    for finger in fin_count.keys():
       for fingerkeys in main_dict[finger].keys():
           print(fingerkeys)
           fin_count[finger] += key_stress[fingerkeys]
    return fin_count