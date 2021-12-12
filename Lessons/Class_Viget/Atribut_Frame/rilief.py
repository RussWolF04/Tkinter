import tkinter as tk

# Создаем словарь с эфектами
border_effects = {
    "flat": tk.FLAT,  # Без эфекта рамки (по умолчанию)
    "sunken": tk.SUNKEN,  # Эфеукт углубление элемента
    "raised": tk.RAISED,  # Эфект выпклости элемента
    "groove": tk.GROOVE,  # Эфект врезанной в текстуру рамки
    "ridge": tk.RIDGE,  # Эфект выпуклой выемки рамки
}

window = tk.Tk()

# Запускаем цикл for для каждого элемента в словаре border_effects
for relief_name, relief in border_effects.items():
    # создает новый виджет Frame и назначает его объекту window
    '''
    Атрибут relief установлен на соответствующий элемент рельефа в словаре border_effects,
    а атрибут border установлен на 5 пикселей, чтобы эффект был видимым
    '''
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)

    # помещает виджет рамки в окно с помощью метода .pack(). Ключевое слово side указывает Tkinter, где поместить рамку
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()