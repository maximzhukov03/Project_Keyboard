from processing import *
from read_files import *
from dicts import *
from GRAF_FINAL import *

shift = 0
alt = 0



current = ["qwer", "ant"]


match current[0]:
    case "qwer":
        first_sh_set = qwertset
        first_alt_set = get_extra_let(qwerty, all_symb)
        first_dict_raskl = put_altlet(qwerty, first_alt_set)
        first_fin_count = dict.fromkeys(main_dict.keys(), 0)
    case "ant":
        first_sh_set = antset
        first_alt_set = get_extra_let(ant, all_symb)
        first_dict_raskl = put_altlet(ant, first_alt_set)
        first_fin_count = dict.fromkeys(main_dict.keys(), 0)
    case "dicktor":
        first_sh_set = dicktorset
        first_alt_set = get_extra_let(dicktor, all_symb)
        first_dict_raskl = put_altlet(dicktor, first_alt_set)
        first_fin_count = dict.fromkeys(main_dict.keys(), 0)
    case "zub":
        first_sh_set = zubset
        first_alt_set = get_extra_let(zub, all_symb)
        first_dict_raskl = put_altlet(zub, first_alt_set)
        first_fin_count = dict.fromkeys(main_dict.keys(), 0)


match current[1]:
    case "qwer":
        second_sh_set = qwertset
        second_alt_set = get_extra_let(qwerty, all_symb)
        second_dict_raskl = put_altlet(qwerty, second_alt_set)
        second_fin_count = dict.fromkeys(main_dict.keys(), 0)
    case "ant":
        second_sh_set = antset
        second_alt_set = get_extra_let(ant, all_symb)
        second_dict_raskl = put_altlet(ant, second_alt_set)
        second_fin_count = dict.fromkeys(main_dict.keys(), 0)
    case "dicktor":
        second_sh_set = dicktorset
        second_alt_set = get_extra_let(dicktor, all_symb)
        second_dict_raskl = put_altlet(dicktor, second_alt_set)
        second_fin_count = dict.fromkeys(main_dict.keys(), 0)
    case "zub":
        second_sh_set = zubset
        second_alt_set = get_extra_let(zub, all_symb)
        second_dict_raskl = put_altlet(zub, second_alt_set)
        second_fin_count = dict.fromkeys(main_dict.keys(), 0)


# Подсчёт символов.
count_symb(read_large_file('voina-i-mir.txt', 1024))


# Подсчёт шифтов для уникальных символов каждой раскладки.
shift_first = dop_shift(first_sh_set, score_symb)
shift_second = dop_shift(second_sh_set, score_symb)
alt_first = dop_alt(first_alt_set, score_symb)
alt_second = dop_alt(second_alt_set, score_symb)


#Создание словарей нагрузки для каждой раскладки.
key_stress_first = dict.fromkeys(first_dict_raskl.values(), 0)
key_stress_second = dict.fromkeys(second_dict_raskl.values(), 0)
# Подсчет нагрузки клавиш для каждой раскладки.
key_stress_first = (key_stress_counter(key_stress_first, score_symb, first_dict_raskl, shift_first, alt_first))
key_stress_second = (key_stress_counter(key_stress_second, score_symb, second_dict_raskl, shift_second, alt_second))


#print(score_symb)
# Подсчет нагрузки для каждого файла
fin_count_first = (finger_stress_counter(first_fin_count, key_stress_first, main_dict, True))
fin_count_second = (finger_stress_counter(second_fin_count, key_stress_second, main_dict, True))




# Подсчёт буквенных сочетаний
gramlist = codesymbols_from_strF(read_large_file("1grams-3.txt", 2024))
gramlist = gram_drobl(gramlist, 3)
#print(gramlist)
grams_friq_first = gram_hendler(gramlist, first_dict_raskl, 3)
grams_friq_second = gram_hendler(gramlist, second_dict_raskl, 3)
#print(grams_friq)
# Вывод графики
GRAF(fin_count_second, fin_count_first, grams_friq_second, grams_friq_first)









