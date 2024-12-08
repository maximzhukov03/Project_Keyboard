import matplotlib.pyplot as plt

def GRAF(ClickANT=None, Click_QWERTY=None, grams_ant=None, grams_qwerty=None):
    #Фигура с тремя графиками
    fig = plt.figure(figsize=(15, 10))
    
    # Верхний график (распределение кликов СТАРАЯ ЛАБА)
    ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
    # Проверка на None если вдруг входные данные отсутствуют
    if ClickANT is None:
        ClickAN = {'fi5l': 0, 'fi4l': 0, 'fi3l': 0, 'fi2l': 0, 'fi1l': 0, 'fi2r': 0, 'fi3r': 0, 'fi4r': 0, 'fi5r': 0}
    if Click_QWERTY is None:
        Click_QWERTY = {'fi5l': 0, 'fi4l': 0, 'fi3l': 0, 'fi2l': 0, 'fi1l': 0, 'fi2r': 0, 'fi3r': 0, 'fi4r': 0, 'fi5r': 0}
    
    FingOrd = ['fi5l', 'fi4l', 'fi3l', 'fi2l', 'fi1l', 'fi2r', 'fi3r', 'fi4r', 'fi5r']
    FingLable = [
        'Левый\nМизинец', 'Левый\nБезымянный', 'Левый\nСредний', 'Левый\nУказательный', 'Левый\nБольшой',
        'Правый\nУказательный', 'Правый\nСредний', 'Правый\nБезымянный', 'Правый\nМизинец'
    ]

    
    left_clicks = [ClickANT[finger] for finger in FingOrd]
    right_clicks = [Click_QWERTY[finger] for finger in FingOrd]
    
    BAR_width = 0.4
    index = range(len(FingLable))
    bars1 = ax1.barh(index, left_clicks, BAR_width, label='АНТ', color='red')
    bars2 = ax1.barh([i + BAR_width for i in index], right_clicks, BAR_width, label='ЙЦУКЕН', color='blue')
    ax1.bar_label(bars1)
    ax1.bar_label(bars2)
    ax1.set_ylabel('Пальцы')
    ax1.set_xlabel('Кол. нажатий')
    ax1.set_title('Распределение кликов по пальцам для левой и правой рук')
    ax1.set_yticks([i + BAR_width / 2 for i in index])
    ax1.set_yticklabels(FingLable)
    ax1.legend()

    # ANT Нижний левый график распределение диграмм
    ax2 = plt.subplot2grid((2, 2), (1, 0))
    # Проверка на None если вдруг входные данные отсутствуют
    if grams_ant is None:
        grams_ant = {'R_Gram_2': 0, 'L_Gram_2': 0, 'QL_Gram_2': 0, 'QR_Gram_2': 0}
    
    gram_keys = ['R_Gram_2', 'L_Gram_2', 'QL_Gram_2', 'QR_Gram_2']
    gram_values = [grams_ant.get(key, 0) for key in gram_keys]
    # Для названия столбцов диаграмм (Нижних)
    labels = ['Правая\nрука', 'Левая\nрука', 'Удобная для дрочки\nлевая', 'Удобная для дрочки\nправая']
    
    bars = ax2.bar(labels, gram_values, color=['red', 'blue', 'green', 'orange'])
    ax2.bar_label(bars, label_type='center', color='white', fontsize=16)
    ax2.set_title('Распределение диграмм\nАНТ')
    ax2.set_ylabel('Количество')
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)

    # ЙЦУКЕН Нижний правый график распределение диграмм
    ax3 = plt.subplot2grid((2, 2), (1, 1))
    # Проверка на None если вдруг входные данные отсутствуют
    if grams_qwerty is None:
        grams_qwerty = {'R_Gram_2': 0, 'L_Gram_2': 0, 'QL_Gram_2': 0, 'QR_Gram_2': 0}
    
    gram_values = [grams_qwerty.get(key, 0) for key in gram_keys]
    # Меняем конфигурацию графика
    bars = ax3.bar(labels, gram_values, color=['red', 'blue', 'green', 'orange'])
    ax3.bar_label(bars, label_type='center', color='white', fontsize=16)
    ax3.set_title('Распределение диграмм\nЙЦУКЕН')
    ax3.set_ylabel('Количество')
    plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)

    plt.tight_layout()
    plt.show()
