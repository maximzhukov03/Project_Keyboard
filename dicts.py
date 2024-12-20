from frozendict import frozendict

# Заполнение frozendict на основе входных данных
qwerty = frozendict({
1105: "41",
49: "02",
33: "02",
50: "03",
34: "03",
51: "04",
8470: "04",
52: "05",
59: "05",
53: "06",
37: "06",
54: "07",
58: "07",
55: "08",
63: "08",
56: "09",
42: "09",
57: "10",
40: "10",
48: "11",
41: "11",
45: "12",
95: "12",
61: "13",
43: "13",
1081: "16",
1094: "17",
1091: "18",
1082: "19",
1077: "20",
1085: "21",
1075: "22",
1096: "23",
1097: "24",
1079: "25",
1093: "26",
1098: "27",
1092: "30",
1099: "31",
1074: "32",
1072: "33",
1087: "34",
1088: "35",
1086: "36",
1083: "37",
1076: "38",
1078: "39",
1101: "40",
92: "43",
47: "43",
1103: "44",
1095: "45",
1089: "46",
1084: "47",
1080: "48",
1090: "49",
1100: "50",
1073: "51",
1102: "52",
46: "53",
44: "53",
32:"57",
0:"42",
39:"0",
60:"0",
62: "0"
})

# Заполнение frozendict на основе новых входных данных
ant = frozendict({
57: "02",
33: "02",
55: "03",
63: "03",
53: "04",
39: "04",
51: "05",
34: "05",
49: "06",
61: "06",
48: "07",
43: "07",
50: "08",
45: "08",
52: "09",
42: "09",
54: "10",
47: "10",
56: "11",
37: "11",
40: "12",
60: "12",
41: "13",
62: "13",
1075: "16",
1087: "17",
1088: "18",
1076: "19",
1084: "20",
1099: "21",
1080: "22",
1103: "23",
1091: "24",
1093: "25",
1094: "26",
1078: "27",
1074: "30",
1085: "31",
1089: "32",
1090: "33",
1083: "34",
1100: "35",
1086: "36",
1077: "37",
1072: "38",
1082: "39",
1079: "40",
92: "41",
95: "41",
1095: "43",
1097: "44",
1081: "45",
1096: "46",
1073: "47",
44: "48",
59: "48",
46: "49",
58: "49",
1102: "50",
1101: "51",
1105: "52",
1092: "53",
32:"57",
0:"42",
8470: "0",
1098: "0"
})

"""
Словарь, связывающий пальцы и кнопки, и содержащий штраф на каждую кнопку
"""


main_dict = frozendict({
    "fi5l": {"41": 3, "02": 2, "16": 1, "30": 0, "42": 2, "44": 1},
    "fi4l": {"03": 2, "17": 1, "31": 0, "45": 1},
    "fi3l": {"04": 2, "18": 1, "32": 0, "46": 1},
    "fi2l": {"05": 2, "19": 1, "33": 0, "47": 1, "06": 3, "20": 2, "34": 1, "48": 1},
    "fi1l": {"57": 0},
    "fi2r": {"07": 3, "21": 2, "35": 1, "49": 1, "08": 2, "22": 1, "36": 0, "50": 1},
    "fi3r": {"09": 2, "23": 1, "37": 0, "51": 1},
    "fi4r": {"10": 2, "24": 1, "38": 0, "52": 1},
    "fi5r": {"11": 2, "12": 3, "13": 4, "25": 1, "26": 2, "27": 3, "43": 4, "39": 0, "40": 1, "53": 1},
})

'''
Словарь для подсчёта символов в файле, 0 - shift
'''
score_symb = {
    49: 0, 33: 0, 50: 0, 34: 0, 51: 0, 8470: 0, 52: 0, 59: 0, 53: 0, 37: 0, 54: 0, 58: 0,
    55: 0, 63: 0, 56: 0, 42: 0, 57: 0, 40: 0, 48: 0, 41: 0, 45: 0, 95: 0, 61: 0, 43: 0,
    1081: 0, 1094: 0, 1091: 0, 1082: 0, 1077: 0, 1085: 0, 1075: 0, 1096: 0, 1097: 0,
    1079: 0, 1093: 0, 1098: 0, 1092: 0, 1099: 0, 1074: 0, 1072: 0, 1087: 0,
    1088: 0, 1086: 0, 1083: 0, 1076: 0, 1078: 0, 1101: 0, 1105: 0, 92: 0, 47: 0, 1103: 0,
    1095: 0, 1089: 0, 1084: 0, 1080: 0, 1090: 0, 1100: 0, 1073: 0, 1102: 0, 46: 0, 44: 0,
    32: 0, 0: 0, 39: 0, 60: 0, 62: 0
}
'''
Словарь для подсчёта нажатия шифта
'''
alfset = frozenset('ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')
#antset = frozenset('_!?`"=+-*/%<>;:')
#qwertset = frozenset('!"№;%:?*()_+,')
antset= {39, 33, 34, 37, 42, 43, 45, 47, 61, 58, 59, 60, 63, 62, 95}
qwertset= {33, 34, 37, 40, 41, 42, 43, 44, 8470, 58, 59, 95, 63}

fin_count_qwer = {
    "fi5l": 0,
    "fi4l": 0,
    "fi3l": 0,
    "fi2l": 0,
    "fi1l": 0,
    "fi2r": 0,
    "fi3r": 0,
    "fi4r": 0,
    "fi5r": 0,
}

fin_count_ant = {
    "fi5l": 0,
    "fi4l": 0,
    "fi3l": 0,
    "fi2l": 0,
    "fi1l": 0,
    "fi2r": 0,
    "fi3r": 0,
    "fi4r": 0,
    "fi5r": 0,
}

