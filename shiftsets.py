from frozendict import frozendict
from ANT import *
from QWERTY import *
from SCORE_SYMB import *
from MAIN_DICT import *
from SHIFT_SETS import *
from FING_COUNT import *
from shiftsets import *
alf = frozenset('ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')
ant = frozenset('_!?`"=+-*/%<>;:')
qwert = frozenset('!"№;%:?*()_+,')
antalf = frozenset(alf | ant)
qweralf = frozenset(alf | qwert)
main_dict = frozendict({
    "fi5l": {"41": 3, "02": 2, "15": 2, "16": 1, "58": 1, "30": 0, "42": 2, "44": 1},
    "fi4l": {"03": 2, "17": 1, "31": 0, "45": 1},
    "fi3l": {"04": 2, "18": 1, "32": 0, "46": 1},
    "fi2l": {"05": 2, "19": 1, "33": 0, "47": 1, "06": 3, "20": 2, "34": 1, "48": 1},
    "fi1l": {"57": 0},
    "fi2r": {"07": 3, "21": 2, "35": 1, "49": 1, "08": 2, "22": 1, "36": 0, "50": 1},
    "fi3r": {"09": 2, "23": 1, "37": 0, "51": 1},
    "fi4r": {"10": 2, "24": 1, "38": 0, "52": 1},
    "fi5r": {"11": 2, "12": 3, "13": 4, "14": 5, "25": 1, "26": 2, "27": 3, "43": 4, "39": 0, "40": 1, "28": 2, "53": 1, "54": 2},
})
print(main_dict)
#for values in main_dict.values:
print(chr(49))
key_stress_ant= dict.fromkeys(ant.values(),0)
key_stress_qwer= dict.fromkeys(qwerty.values(),0)

def key_stress_counter(key_stress:dict,stress_sumbol:dict,rascl:dict):
    for symb in stress_sumbol.keys():
        key_stress[rascl[symb]]=stress_sumbol[symb]
    return key_stress