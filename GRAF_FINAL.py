import matplotlib.pyplot as plt


def GRAF(ClickANT, Click_QWERTY):
    
    FingOrd = ['fi5l', 'fi4l', 'fi3l', 'fi2l', 'fi1l', 'fi1r', 'fi2r', 'fi3r', 'fi4r', 'fi5r']
    FingLable = [
        'Левый\nМизинец', 'Левый\nБезымянный', 'Левый\nСредний', 'Левый\nУказательный', 'Левый\nБольшой', 
        'Правый\nБольшой', 'Правый\nУказательный', 'Правый\nСредний', 'Правый\nБезымянный', 'Правый\nМизинец'
    ]
    
    left_clicks = [ClickANT[finger] for finger in FingOrd]
    right_clicks = [Click_QWERTY[finger] for finger in FingOrd]
    
    fig, os = plt.subplots(figsize=(10, 6))
    BAR_width = 0.4
    index = range(len(FingLable))

    os.bar(index, left_clicks, BAR_width, label='ANT', color='red')
    os.bar([i + BAR_width for i in index], right_clicks, BAR_width, label='QWERTY', color='blue')

    os.set_xlabel('Пальцы')
    os.set_ylabel('Кол. нажатий')
    os.set_title('Распределение кликов по пальцам для левой и правой рук')
    os.set_xticks([i + BAR_width / 2 for i in index])
    os.set_xticklabels(FingLable)
    os.legend()

    plt.tight_layout()
    plt.show()

ClickANT = {'fi5l': 272147, 'fi4l': 103082, 'fi3l': 358911, 'fi2l': 870929, 'fi1l': 561472, 
                  'fi1r': 0, 'fi2r': 891155, 'fi3r': 204761, 'fi4r': 111882, 'fi5r': 249743}
Click_QWERTY = {'fi5l': 300000, 'fi4l': 150000, 'fi3l': 400000, 'fi2l': 900000, 'fi1l': 600000,
                     'fi1r': 0, 'fi2r': 850000, 'fi3r': 210000, 'fi4r': 120000, 'fi5r': 260000}

GRAF(ClickANT, Click_QWERTY)
