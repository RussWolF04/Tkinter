import tkinter as tk

# Создаем окно
window = tk.Tk()
# Создаем ярлык
label = tk.Label(text='Name')
# Создаем однострочное текстовое поле
entry = tk.Entry()
# Получаем информацию от пользователя и присвоеваем ее переменной name
name = entry.get()

label.pack()
entry.pack()
window.mainloop()