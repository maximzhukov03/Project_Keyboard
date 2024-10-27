import matplotlib.pyplot as plt

def READ(file):
    with open(file, "r", encoding="utf-8") as file:
        text = file.read()
    return text

RightH = {
    'f1': set("щзжёэё,."),
    'f2': set("дл09"),
    'f3': set("оь8"),
    'f4': set("нгтшщ7"),
    'f5': set(" ")
}

LeftH = {
    'f1': set("йфя1"),
    'f2': set("цыч2"),
    'f3': set("увс3"),      
    'f4': set("камепр456"),
}

spec = set(";,?-.:!\"'()\t\n")

LeftHClick = {'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0}
RightHClick = {'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0}

def CLICK(txt):
    for i in txt.lower():
        if i in spec:
            continue

        for fin, char in LeftH.items():
            if i in char:
                LeftHClick[fin] += 1

        for fin, char in RightH.items():
            if i in char:
                RightHClick[fin] += 1

text = READ("voina-i-mir.txt")
CLICK(text)

print("Левая рука:", LeftHClick)
print("Правая рука:", RightHClick)


fin = ['Миз', 'Безым', 'Сред', 'Указат', 'Пр Больш.']
LeftHClickGist = [LeftHClick['f1'], LeftHClick['f2'], LeftHClick['f3'], LeftHClick['f4'], LeftHClick['f5']]
RightHClickGist = [RightHClick['f1'], RightHClick['f2'], RightHClick['f3'], RightHClick['f4'], RightHClick['f5']]


fig, os = plt.subplots(figsize=(10, 6))
BAR_width = 0.4
index = range(len(fin))


os.bar(index, LeftHClickGist, BAR_width, label='Левая рука', color='red')
os.bar([i + BAR_width for i in index], RightHClickGist, BAR_width, label='Правая рука', color='blue')

os.set_xlabel('Пальцы')
os.set_ylabel('Кол. нажатий')
os.set_title('Распределение кликов по пальцам для левой и правой рук (Раскладка QWERTY)')
os.set_xticks([i + BAR_width / 2 for i in index])
os.set_xticklabels(fin)
os.legend()

plt.tight_layout()
plt.show()
