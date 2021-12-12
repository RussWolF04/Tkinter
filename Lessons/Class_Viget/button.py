import tkinter as tk

window = tk.Tk()  # Создаем окно

# Создаем кнопку
button = tk.Button(
    text="Нажми на меня!",
    width=25,  # Ширина кнопки
    height=5,  # Высота кнопки
    bg="blue",  # Цвет кнопки
    fg="yellow",  # Цвет текста кнопки
)

button.pack()
window.mainloop()