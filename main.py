from functions import *
from dicts import *
shift = 0
count_symb(read_large_file('d:/Институт/PYTHON/Травов/voina-i-mir.txt', 1024))
shift_qwer = dop_shift(qwertset, score_symb)
shift_ant = dop_shift(antset, score_symb)
print(key_stress_counter(key_stress_qwer, score_symb, qwerty, shift_qwer))
print(key_stress_counter(key_stress_ant, score_symb, ant, shift_ant))
print(finger_stress_counter(fin_count_qwer, key_stress_qwer, main_dict))
print(finger_stress_counter(fin_count_ant, key_stress_ant, main_dict))