import matplotlib.pyplot as plt

def GRAF(ClickANT, Click_QWERTY):
    FingOrd = ['fi5l', 'fi4l', 'fi3l', 'fi2l', 'fi1l', 'fi1r', 'fi2r', 'fi3r', 'fi4r', 'fi5r']
    FingLable = [
        'Левый\nМизинец', 'Левый\nБезымянный', 'Левый\nСредний', 'Левый\nУказательный', 'Левый\nБольшой', 
        'Правый\nБольшой', 'Правый\nУказательный', 'Правый\nСредний', 'Правый\nБезымянный', 'Правый\nМизинец'
    ]

    left_clicks = [ClickANT[finger] for finger in FingOrd]
    right_clicks = [Click_QWERTY[finger] for finger in FingOrd]
    
    fig, os = plt.subplots(figsize=(12, 8))
    BAR_width = 0.4 # Ширина
    index = range(len(FingLable))
    os.barh(index, left_clicks, BAR_width, label='ANT', color='red')
    os.barh([i + BAR_width for i in index], right_clicks, BAR_width, label='QWERTY', color='blue')
    os.set_ylabel('Пальцы')
    os.set_xlabel('Количество нажатий')
    os.set_title('Распределение кликов по пальцам для левой и правой рук (Горизонтальный график)')
    os.set_yticks([i + BAR_width / 2 for i in index])
    os.set_yticklabels(FingLable)
    os.legend()
    plt.tight_layout()
    plt.show()
