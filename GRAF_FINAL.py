import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def get_names():
    # Создаем главное окно для ввода
    root = tk.Tk()
    root.withdraw()  # Скрываем главное окно

    # Запрашиваем названия
    name1 = simpledialog.askstring("Ввод", "Введите название 1:")
    name2 = simpledialog.askstring("Ввод", "Введите название 2:")

    if not name1 or not name2:
        messagebox.showerror("Ошибка", "Названия не могут быть пустыми.")
        return None, None

    return name1, name2

def open_graph_window(graph_function, *args):
    new_window = tk.Toplevel()
    new_window.title("График")
    
    fig = graph_function(*args)
    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def open_graph_window(graph_function, *args):
    # Создаем новое окно
    new_window = tk.Toplevel()
    new_window.title("График")
    
    fig = graph_function(*args)
    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def GRAF(ClickANT=None, Click_QWERTY=None, grams_ant=None, grams_qwerty=None):
    name1, name2 = get_names()
    # Создаем главное окно
    root = tk.Tk()
    root.title("Выбор графика")

    # Кнопки для открытия графиков
    btn_click_distribution = tk.Button(root, text="Распределение кликов", 
                                        command=lambda: open_graph_window(plot_click_distribution, ClickANT, Click_QWERTY, name1, name2))
    btn_click_distribution.pack(pady=10)

    btn_grams_ant = tk.Button(root, text=f"Диграммы {name1}", 
                               command=lambda: open_graph_window(plot_grams_ant, grams_ant, name1))
    btn_grams_ant.pack(pady=10)

    btn_grams_qwerty = tk.Button(root, text=f"Диграммы {name2}", 
                                  command=lambda: open_graph_window(plot_grams_qwerty, grams_qwerty, name2))
    btn_grams_qwerty.pack(pady=10)

    root.mainloop()

def plot_click_distribution(ClickANT=None, Click_QWERTY=None, name1=None, name2=None, save_path="click_distribution.png"):
    fig = plt.figure(figsize=(15, 10))
    ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)

    # Проверка на None если вдруг входные данные отсутствуют
    if ClickANT is None:
        ClickANT = {'fi5l': 0, 'fi4l': 0, 'fi3l': 0, 'fi2l': 0, 'fi1l': 0, 'fi1r': 0, 'fi2r': 0, 'fi3r': 0, 'fi4r': 0, 'fi5r': 0}
    if Click_QWERTY is None:
        Click_QWERTY = {'fi5l': 0, 'fi4l': 0, 'fi3l': 0, 'fi2l': 0, 'fi1l': 0, 'fi1r': 0, 'fi2r': 0, 'fi3r': 0, 'fi4r': 0, 'fi5r': 0}

    FingOrd = ['fi5l', 'fi4l', 'fi3l', 'fi2l', 'fi1l', 'fi1r', 'fi2r', 'fi3r', 'fi4r', 'fi5r']
    FingLable = [
        'Левый\nМизинец', 'Левый\nБезымянный', 'Левый\nСредний', 'Левый\nУказательный', 'Левый\nБольшой', "Правый\nБольшой",
        'Правый\nУказательный', 'Правый\nСредний', 'Правый\nБезымянный', 'Правый\nМизинец'
    ]

    left_clicks = [ClickANT[finger] for finger in FingOrd]
    right_clicks = [Click_QWERTY[finger] for finger in FingOrd]

    BAR_width = 0.4
    index = range(len(FingLable))
    bars1 = ax1.barh(index, left_clicks, BAR_width, label=name1, color='red')
    bars2 = ax1.barh([i + BAR_width for i in index], right_clicks, BAR_width, label=name2, color='blue')
    ax1.bar_label(bars1)
    ax1.bar_label(bars2)
    ax1.set_ylabel('Пальцы')
    ax1.set_xlabel('Кол. нажатий')
    ax1.set_title('Распределение кликов по пальцам для левой и правой рук')
    ax1.set_yticks([i + BAR_width / 2 for i in index])
    ax1.set_yticklabels(FingLable)
    ax1.legend()

    fig.savefig(save_path)
    plt.close(fig)  # Закрываем фигуру, чтобы освободить память
    return fig

def plot_grams_ant(grams_ant=None, name1=None, save_path=f"grams_ant.png"):
    fig = plt.figure(figsize=(7, 5))
    ax2 = plt.subplot(111)

    # Проверка на None если вдруг входные данные отсутствуют
    if grams_ant is None:
        grams_ant = {'R_Gram_': 0, 'L_Gram_': 0, 'QL_Gram_': 0, 'QR_Gram_': 0}

    gram_keys = ['R_Gram_', 'L_Gram_', 'QL_Gram_', 'QR_Gram_']
    gram_values = [grams_ant.get(key, 0) for key in gram_keys]
    
    labels = ['Правая\nрука', 'Левая\nрука', 'Удобная\nлевая', 'Удобная\nправая']
    bars = ax2.bar(labels, gram_values, color=['red', 'blue', 'green', 'orange'])
    ax2.bar_label(bars, label_type='center', color='white', fontsize=16)
    ax2.set_title(f'Распределение диграмм\n{name1}')
    ax2.set_ylabel('Количество')

    # Сохранение графика в файл
    fig.savefig(f"graf_{name1}.png")
    plt.close(fig)  # Закрываем фигуру, чтобы освободить память
    return fig

def plot_grams_qwerty(grams_qwerty=None, name2=None):
    fig = plt.figure(figsize=(7, 5))
    ax3 = plt.subplot(111)

    # Проверка на None если вдруг входные данные отсутствуют
    if grams_qwerty is None:
        grams_qwerty = {'R_Gram_': 0, 'L_Gram_': 0, 'QL_Gram_': 0, 'QR_Gram_': 0}

    gram_keys = ['R_Gram_', 'L_Gram_', 'QL_Gram_', 'QR_Gram_']
    gram_values = [grams_qwerty.get(key, 0) for key in gram_keys]
    
    labels = ['Правая\nрука', 'Левая\nрука', 'Удобная\nлевая', 'Удобная\nправая']
    bars = ax3.bar(labels, gram_values, color=['red', 'blue', 'green', 'orange'])
    ax3.bar_label(bars, label_type='center', color='white', fontsize=16)
    ax3.set_title(f'Распределение диграмм\n{name2}')
    ax3.set_ylabel('Количество')

    # Сохранение графика в файл
    fig.savefig(f"graf_{name2}.png")
    plt.close(fig)  # Закрываем фигуру, чтобы освободить память
    return fig
