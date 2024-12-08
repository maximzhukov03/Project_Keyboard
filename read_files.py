from dicts import *


def read_large_file(file_path: str, chunk_size: int):
    """
    Генераторная функция, обрабатывающая текст по кускам.

    Эта функция читает файл указанного пути и возвращает его содержимое 
    по частям (чанками) заданного размера. Это позволяет эффективно 
    обрабатывать большие файлы, не загружая их целиком в память.

    Параметры:
    file_path (str): Путь к файлу, который необходимо прочитать.
    chunk_size (int): Размер чанка в байтах, который будет считываться за один раз.

    Возвращает:
    generator: Генератор, который поочередно возвращает чанки текста 
               из файла до тех пор, пока файл не будет полностью прочитан.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk


def count_symb(generator):
    """
    Функция подсчёта символов.

    На вход получает генератор, обрабатывающий файл, и возвращает словарь,
    в котором ключами являются символы, а значениями — их количество.

    Параметры:
    generator (iterator): Генератор, который возвращает чанки текста из файла.

    Возвращает:
    dict: Словарь, где ключами являются символы (str), а значениями — 
          количество их вхождений (int). Также учитывается общее количество 
          символов, соответствующих определённым условиям.
    """
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


def dop_shift(set_shift:set,symbol_strees:dict):
    """
    Подсчёт шифтов для уникальных символов.

    Эта функция принимает множество уникальных символов и словарь, 
    в котором хранятся значения для каждого символа. 
    Она возвращает сумму шифтов для всех символов из множества.

    Параметры:
    set_shift (set): Множество уникальных символов, для которых необходимо 
                     подсчитать шифты.
    symbol_strees (dict): Словарь, где ключами являются коды символов, 
                          а значениями — соответствующие значения шифтов (int).

    Возвращает:
    shift (int): Сумма шифтов для всех уникальных символов из set_shift.
    """
    shift=0
    for sym in set_shift:
        shift+=symbol_strees[sym]
    return shift

