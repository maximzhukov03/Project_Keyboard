import unittest
from dicts import *
from unittest.mock import mock_open, patch
from processing import *
from read_files import *


class TestReadLargeFile(unittest.TestCase):
    
    def test_read_large_file(self):
        mock_file_content = "This is a test file with multiple lines of text for testing purposes."
        chunk_size = 10  
        expected_chunks = [
            "This is a ",
            "test file ",
            "with multi",
            "ple lines ",
            "of text fo",
            "r testing ",
            "purposes."
        ]

        with patch("builtins.open", mock_open(read_data = mock_file_content)) as mock_file:
            result = list(read_large_file("fake_path.txt", chunk_size))
            self.assertEqual(result, expected_chunks)
            mock_file.assert_called_once_with("fake_path.txt", 'r', encoding = 'utf-8')


class TestCountSymb(unittest.TestCase):
    # def setUp(self):
      #  for key in score_symb:
      #      score_symb[key] = 0
    def test_count_symb(self):

        
        def test_generator():
            yield "Привет, мир!"
            yield "Тест строки 123"

        
        expected_result = {
            49: 1, 33: 1, 50: 1, 34: 0, 51: 1, 8470: 0, 52: 0, 59: 0, 53: 0, 37: 0, 54: 0, 58: 0,
            55: 0, 63: 0, 56: 0, 42: 0, 57: 0, 40: 0, 48: 0, 41: 0, 45: 0, 95: 0, 61: 0, 43: 0,
            1081: 0, 1094: 0, 1091: 0, 1082: 1, 1077: 2, 1085: 0, 1075: 0, 1096: 0, 1097: 0,
            1079: 0, 1093: 0, 1098: 0, 1092: 0, 1099: 0, 1074: 1, 1072: 0, 1087: 1,
            1088: 3, 1086: 1, 1083: 0, 1076: 0, 1078: 0, 1101: 0, 1105: 0, 92: 0, 47: 0, 1103: 0,
            1095: 0, 1089: 2, 1084: 1, 1080: 3, 1090: 4, 1100: 0, 1073: 0, 1102: 0, 46: 0, 44: 1,
            32: 3, 0: 2, 39: 0, 60: 0, 62: 0
        }
        
        result = count_symb(test_generator())
        self.assertEqual(result, expected_result)


class TestDopShift(unittest.TestCase):
    def test_dop_shift(self):
        # global symb_count
        symb_count = {
            49: 1, 33: 2, 50: 1, 34: 3, 51: 0, 8470: 0, 52: 0, 59: 0, 53: 0, 37: 0, 54: 0, 58: 0,
            55: 0, 63: 0, 56: 0, 42: 0, 57: 0, 40: 0, 48: 0, 41: 0, 45: 0, 95: 0, 61: 0, 43: 0,
            1081: 0, 1094: 0, 1091: 0, 1082: 1, 1077: 2, 1085: 0, 1075: 0, 1096: 0, 1097: 0,
            1079: 0, 1093: 0, 1098: 0, 1092: 0, 1099: 0, 1074: 1, 1072: 0, 1087: 1,
            1088: 3, 1086: 1, 1083: 0, 1076: 0, 1078: 0, 1101: 0, 1105: 0, 92: 0, 47: 0, 1103: 0,
            1095: 0, 1089: 2, 1084: 1, 1080: 3, 1090: 4, 1100: 0, 1073: 0, 1102: 0, 46: 0, 44: 1,
            32: 3, 0: 2, 39: 0, 60: 0, 62: 0
        }
        result = dop_shift(antset, symb_count)
        self.assertEqual(result, 5)


class TestKeyStressCounter(unittest.TestCase):
    def test_key_stress_counter(self):
        # global key_stress
        key_stress = {
             '02': 3, '03': 4, '04': 0, '05': 0, '06': 0,
             '07': 0, '08': 0, '09': 0, '10': 0, '11': 0,
             '12': 0, '13': 0, '16': 0, '17': 0, '18': 0,
             '19': 1, '20': 2, '21': 0, '22': 0, '23': 0,
             '24': 0, '25': 0, '26': 0, '27': 0, '30': 0,
             '31': 0, '32': 1, '33': 0, '34': 1, '35': 3,
             '36': 1, '37': 0, '38': 0, '39': 0, '40': 0,
             '41': 0, '43': 0, '44': 0, '45': 0, '46': 2,
             '47': 1, '48': 3, '49': 4, '50': 0, '51': 0,
             '52': 0, '53': 1, '57': 3, '42': 5, '0': 0
        }
        # что-то с о
        symb_count = {
            49: 1, 33: 2, 50: 1, 34: 3, 51: 0, 8470: 0, 52: 0, 59: 0, 53: 0, 37: 0, 54: 0, 58: 0,
            55: 0, 63: 0, 56: 0, 42: 0, 57: 0, 40: 0, 48: 0, 41: 0, 45: 0, 95: 0, 61: 0, 43: 0,
            1081: 0, 1094: 0, 1091: 0, 1082: 1, 1077: 2, 1085: 0, 1075: 0, 1096: 0, 1097: 0,
            1079: 0, 1093: 0, 1098: 0, 1092: 0, 1099: 0, 1074: 1, 1072: 0, 1087: 1,
            1088: 3, 1086: 1, 1083: 0, 1076: 0, 1078: 0, 1101: 0, 1105: 0, 92: 0, 47: 0, 1103: 0,
            1095: 0, 1089: 2, 1084: 1, 1080: 3, 1090: 4, 1100: 0, 1073: 0, 1102: 0, 46: 0, 44: 1,
            32: 3, 0: 0, 39: 0, 60: 0, 62: 0
        }
        result = key_stress_counter(key_stress_qwer, symb_count, qwerty, 5)
        self.assertEqual(result, key_stress)


class TestFingerStress_counter(unittest.TestCase):
    def test_finger_stress_counter(self):
        fin_count_qwer = {
            "fi5l": 8,
            "fi4l": 4,
            "fi3l": 3,
            "fi2l": 8,
            "fi1l": 3,
            "fi2r": 8,
            "fi3r": 0,
            "fi4r": 0,
            "fi5r": 1,
        }
        key_stress = {
             '02': 3, '03': 4, '04': 0, '05': 0, '06': 0,
             '07': 0, '08': 0, '09': 0, '10': 0, '11': 0,
             '12': 0, '13': 0, '16': 0, '17': 0, '18': 0,
             '19': 1, '20': 2, '21': 0, '22': 0, '23': 0,
             '24': 0, '25': 0, '26': 0, '27': 0, '30': 0,
             '31': 0, '32': 1, '33': 0, '34': 1, '35': 3,
             '36': 1, '37': 0, '38': 0, '39': 0, '40': 0,
             '41': 0, '43': 0, '44': 0, '45': 0, '46': 2,
             '47': 1, '48': 3, '49': 4, '50': 0, '51': 0,
             '52': 0, '53': 1, '57': 3, '42': 5, '0': 0
        }
        result = finger_stress_counter(fin_count_qwer, key_stress, main_dict)
        self.assertEqual(result, fin_count_qwer)


if __name__ == '__main__':
    unittest.main()
