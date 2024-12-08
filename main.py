from processing import *
from read_files import *
from dicts import *
from GRAF_FINAL import *

shift = 0


# Подсчёт символов.
count_symb(read_large_file('voina-i-mir.txt', 1024))


# Подсчёт шифтов для уникальных символов каждой раскладки.
shift_qwer = dop_shift(qwertset, score_symb)
shift_ant = dop_shift(antset, score_symb)


#Создание словарей нагрузки для каждой раскладки.
key_stress_ant = dict.fromkeys(ant.values(),0)
key_stress_qwer = dict.fromkeys(qwerty.values(),0)


# Подсчет нагрузки клавиш для каждой раскладки.
key_stress_qwer = (key_stress_counter(key_stress_qwer, score_symb, qwerty, shift_qwer))
key_stress_ant = (key_stress_counter(key_stress_ant, score_symb, ant, shift_ant))


# Подсчет нагрузки для каждого файла
fin_count_qwer = (finger_stress_counter(fin_count_qwer, key_stress_qwer, main_dict, True))
fin_count_ant = (finger_stress_counter(fin_count_ant, key_stress_ant, main_dict, True))


# Подсчёт буквенных сочетаний
gramlist = codesymbols_from_strF(read_large_file("grams.txt", 2024))
#print(gramlist)
grams_friq_qwer = gram_hendler(gramlist,qwerty,2)
grams_friq_ant = gram_hendler(gramlist,ant,2)
#print(grams_friq)
# Вывод графики
GRAF(fin_count_ant, fin_count_qwer, grams_friq_ant,grams_friq_qwer)









