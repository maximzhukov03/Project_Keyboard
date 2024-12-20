from frozendict import frozendict

import dicts
from dicts import *

def key_stress_counter(key_stress:dict,stress_sumbol:dict,rascl:dict,shift:int,alt:int):
    '''
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
    '''
    for symb in stress_sumbol.keys():
        key_stress[rascl[symb]]+=stress_sumbol[symb]
    key_stress["42"]+=shift
    key_stress["100"]+=alt
    return key_stress 


def finger_stress_counter(fin_count:dict,key_stress:dict,main_dict:frozendict,check:bool):
    '''
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
    '''
    for finger in fin_count.keys():
       for fingerkeys in main_dict[finger].keys():
           if check:
               shtraf=(main_dict[finger][fingerkeys]+1)*check
           else:
               shtraf=1
           fin_count[finger] += key_stress[fingerkeys]*shtraf
    return fin_count


#подсчёт буквенных сочетаний


def key_quality(gramlist_key, arm: str,gramlen:int):
    match arm:
        case "R": #2-5
            f5 = set(main_dict["fi5r"].keys())
            f4 = set(main_dict["fi4r"].keys())
            f3 = set(main_dict["fi3r"].keys())
            f2 = set(main_dict["fi2r"].keys())
            fi = [f5, f4, f3, f2]
        case "L": #5-2
            f5 = set(main_dict["fi5l"].keys())
            f4 = set(main_dict["fi4l"].keys())
            f3 = set(main_dict["fi3l"].keys())
            f2 = set(main_dict["fi2l"].keys())
            fi = [f5, f4, f3, f2]
    flag = 0
    print(gramlist_key)
    for el in gramlist_key:
        for _ in fi:
            if flag == gramlen:
                return True
            print(fi[0])
            if el in fi[0]:
                print("true")
                flag += 1
                fi.pop(0)
                break
            else:
                print("not in", el)
                fi.pop(0)
    if flag == gramlen:
        return True
    else:
        return False

def gram_hendler(gramlist: list, layout: frozendict, gramlen: int):
    Gram_len = [x+"_"+str(gramlen) for x in gramnameset]
    Gram_counter=dict.fromkeys(Gram_len,0)
    for graminnerlist in gramlist:

        gramlist_key = [layout[x] for x in graminnerlist]

        if all(el in left for el in gramlist_key):
            Gram_counter["L_Gram"+"_"+str(gramlen)] += 1
            if key_quality(gramlist_key, 'L',gramlen):
                Gram_counter["QL_Gram"+"_"+str(gramlen)] +=1
        if all(el in right for el in gramlist_key):
            Gram_counter["R_Gram"+"_"+str(gramlen)] += 1
            if key_quality(gramlist_key, 'R',gramlen):
                Gram_counter["QR_Gram" + "_" + str(gramlen)] += 1

    return Gram_counter



#общий счётчик сочетаний 
def codesymbols_from_strF(generator):
    gramlist=[]
    for chunk in generator:
        chunk = chunk.splitlines()
        for str in chunk:
            strStrip = str.strip()
            if not strStrip:
                continue
            gramlist.append([ord(elem) for elem in strStrip])
    return gramlist

def gram_drobl(word_list:list,gramlen:int):
    gram_list = []
    for word in word_list:
        gram = []
        for elem in word:
            gram.append(elem)
            if len(gram) == gramlen:
                gram_list.append(gram)
                gram = [gram[1]]
    return gram_list

