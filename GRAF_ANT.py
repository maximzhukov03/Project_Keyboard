import matplotlib.pyplot as plt

def READ(file):
    with open(file, "r", encoding="utf-8") as file:
        text = file.read()
    return text

RightHANT = {
    'f1': set("хцжчкзф8"),
    'f2': set("уаё6"),
    'f3': set("яеэ4"),
    'f4': set("ыьиою02"),
    'f5': set(" ")
}

LeftHANT = {
    'f1': set("гвц9"),
    'f2': set("пнй7"),
    'f3': set("рсш5"),      
    'f4': set("дтбмл13"),
}

RightHQWERTY = {
    'f1': set("щзжёэё,."),
    'f2': set("дл09"),
    'f3': set("оь8"),
    'f4': set("нгтшщ7"),
    'f5': set(" ")
}

LeftHQWERTY = {
    'f1': set("йфя1"),
    'f2': set("цыч2"),
    'f3': set("увс3"),      
    'f4': set("камепр456"),
}

spec = set(";,?-.:!\"'()\t\n")

LeftHClickANT = {'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0}
RightHClickANT = {'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0}

LeftHClickQWERTY = {'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0}
RightHClickQWERTY = {'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0, 'f5': 0}

def CLICK(txt, LeftH, RightH, LeftHClick, RightHClick):
    for i in txt.lower():
        if i in spec:
            continue

        for fin, char in LeftH.items():
            if i in char:
                LeftHClick[fin] += 1

        for fin, char in RightH.items():
            if i in char:
                RightHClick[fin] += 1
    return LeftHClick, RightHClick

text = READ("voina-i-mir.txt")

LeftHClickANT, RightHClickANT = CLICK(text, LeftHANT, RightHANT, LeftHClickANT, RightHClickANT)

LeftHClickQWERTY, RightHClickQWERTY = CLICK(text, LeftHQWERTY, RightHQWERTY, LeftHClickQWERTY, RightHClickQWERTY)

print(LeftHClickANT, "\n" ,RightHClickANT)
print(LeftHClickQWERTY, "\n" ,RightHClickQWERTY)

fin = ['Левый\nМизинец', 'Левый\nБезымянный', 'Левый\nСредний', 'Левый\nУказательный', 'Левый\nБольшой', 
       'Правый\nБольшой', 'Правый\nУказательный', 'Правый\nСредний', 'Правый\nБезымянный', 'Правый\nМизинец']

LeftHClickGistANT_QWERTY = [
    LeftHClickANT['f1'], LeftHClickANT['f2'],
    LeftHClickANT['f3'], LeftHClickANT['f4'], 
    LeftHClickANT['f5'], 
    RightHClickANT['f5'], RightHClickANT['f4'], 
    RightHClickANT['f3'], RightHClickANT['f2'], 
    RightHClickANT['f1']
]

RightHClickGistANT_QWERTY = [
    LeftHClickQWERTY['f1'], LeftHClickQWERTY['f2'], 
    LeftHClickQWERTY['f3'], LeftHClickQWERTY['f4'], 
    LeftHClickQWERTY['f5'], 
    RightHClickQWERTY['f5'], RightHClickQWERTY['f4'], 
    RightHClickQWERTY['f3'], RightHClickQWERTY['f2'], 
    RightHClickQWERTY['f1']
]

fig, os = plt.subplots(figsize=(10, 6))
BAR_width = 0.4
index = range(len(fin))


os.bar(index, LeftHClickGistANT_QWERTY, BAR_width, label='ANT', color='red')
os.bar([i + BAR_width for i in index], RightHClickGistANT_QWERTY, BAR_width, label='QWERTY', color='blue')

os.set_xlabel('Пальцы')
os.set_ylabel('Кол. нажатий')
os.set_title('Распределение кликов по пальцам для левой и правой рук')
os.set_xticks([i + BAR_width / 2 for i in index])
os.set_xticklabels(fin)
os.legend()

plt.tight_layout()
plt.show()
