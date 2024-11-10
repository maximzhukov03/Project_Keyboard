from dicts import *


def key_stress_counter(key_stress:dict,stress_sumbol:dict,rascl:dict,shift:int):
"""
    Функция подсчета нагрузки клавиш.

    Эта функция обновляет словарь key_stress, добавляя значения нагрузки 
    из словаря stress_sumbol для соответствующих символов, преобразованных 
    с помощью словаря rascl. Также учитывается нажатие клавиши шифт.

    Параметры:
    key_stress (dict): Словарь, в который будут добавлены значения нагрузки. 
                       Ключи — это код клавиши, а значения — 
                       соответствующие суммы нагрузки (int).
    stress_sumbol (dict): Словарь, где ключами являются коды символов, а значениями — 
                          их количество (int).
    rascl (dict): Словарь, который сопоставляет символы из stress_sumbol 
                  с идентификаторами в key_stress.
    shift (int): Дополнительное значение, которое будет добавлено к ключу "42" 
                 в словаре key_stress.

    Возвращает:
    dict: Обновлённый словарь key_stress с добавленными значениями нагрузки.
"""
    for symb in stress_sumbol.keys():
        key_stress[rascl[symb]]+=stress_sumbol[symb]
    key_stress["42"]+=shift
    return key_stress 


def finger_stress_counter(fin_count:dict,key_stress:dict,main_dict:frozendict,check:bool):
"""
    Подсчёт нагрузки для каждого пальца.

    Эта функция обновляет словарь fin_count, добавляя значения нагрузки 
    для каждого пальца, учитывая соответствующие ключи из key_stress 
    и значения из main_dict. Если параметр check установлен в True, 
    применяется штраф к значению стресса.

    Параметры:
    fin_count (dict): Словарь, в который будут добавлены значения нагрузки 
                      для каждого пальца. Ключи — это идентификаторы пальцев, 
                      а значения — соответствующие суммы стресса (int).
    key_stress (dict): Словарь, где ключами являются идентификаторы ключей, 
                       а значениями — их значения нагрузки (int).
    main_dict (frozendict): Словарь, который сопоставляет пальцы с их 
                             соответствующими ключами и значениями.
    check (bool): Флаг, указывающий, нужно ли применять штраф. Если True, 
                  применяется штраф к значению стресса.

    Возвращает:
    dict: Обновлённый словарь fin_count с добавленными значениями нагрузки
"""
    for finger in fin_count.keys():
       for fingerkeys in main_dict[finger].keys():
           if check:
               shtraf=(main_dict[finger][fingerkeys]+1)*check
           else:
               shtraf=1
           fin_count[finger] += key_stress[fingerkeys]*shtraf
    return fin_count