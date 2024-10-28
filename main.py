from functions import *
from dicts import *
from GRAF_FINAL import *
shift = 0
count_symb(read_large_file('voina-i-mir.txt', 1024))
shift_qwer = dop_shift(qwertset, score_symb)
shift_ant = dop_shift(antset, score_symb)
key_stress_ant = dict.fromkeys(ant.values(),0)
key_stress_qwer = dict.fromkeys(qwerty.values(),0)
key_stress_qwer = (key_stress_counter(key_stress_qwer, score_symb, qwerty, shift_qwer))
key_stress_ant = (key_stress_counter(key_stress_ant, score_symb, ant, shift_ant))
fin_count_qwer = (finger_stress_counter(fin_count_qwer, key_stress_qwer, main_dict))
fin_count_ant = (finger_stress_counter(fin_count_ant, key_stress_ant, main_dict))
GRAF(fin_count_ant, fin_count_qwer)
