import matplotlib.pyplot as plt


def GRAF(ClickANT, Click_QWERTY):
    
    FingOrd = ['fi5l', 'fi4l', 'fi3l', 'fi2l', 'fi1l', 'fi2r', 'fi3r', 'fi4r', 'fi5r']
    FingLable = [
        'Левый\nМизинец', 'Левый\nБезымянный', 'Левый\nСредний', 'Левый\nУказательный', 'Левый\nБольшой',
        'Правый\nУказательный', 'Правый\nСредний', 'Правый\nБезымянный', 'Правый\nМизинец'
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

