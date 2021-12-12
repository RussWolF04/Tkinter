import tkinter as tk

# window = tk.Tk()
#
# # скрипт создает сетку из рамок 3 × 3 с находящимися в них ярлыками с текстом:
# for i in range(3):  # Цикл будет создавать горизонтальные строки 'row'
#     for j in range(3):  # Цикл создает вертикальные колонки 'column'
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j)  # 3 x 3 row and column
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()
#
# window.mainloop()

'''
Будем использовать отступы вокруг яцеек сетки используя атрибуты 'padx' и 'pady'
'''
# window = tk.Tk()
#
# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         # Добавляем горизонтальные и вертикальные отступы между ячейками 'padx' и 'pady'
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()
#
# window.mainloop()

'''
Атрибуты 'padx' и 'pady' можно использовать так же в методе (менеджере) .pack(), это нам даст
больше отступов по вертикали и горизонтали.
'''
# window = tk.Tk()
#
# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack(padx=5, pady=5)  # Добавляем к методу .pack() атрибуты 'padx' и 'pady'
#         '''
#         Дополнительные отступы вокруг ярлыков с текстом немного расширяют место для
#         каждой ячейки в сетке между рамкой Frame и текстом на ярлыке Label
#         '''
#
# window.mainloop()

# window = tk.Tk()
#
# for i in range(3):
#     '''
#     Метод .columnconfigure() и .rowconfigure() помещаются в тело внешнего цикла for.
#     Можно точно настроить каждый столбец и строку за пределами цикла for, однако для
#     этого нужно будет написать дополнительные шесть строк кода.
#     '''
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)
#     '''
#     В каждой итерации цикла i-ые столбцы и строки настраиваются таким образом, чтобы
#     значение их weight было равно 1. Это является гарантией того, что каждая строка и
#     столбец расширяются с одинаковой скоростью при изменении размера окна. Аргумент
#     minsize имеет значение 75 для каждого столбца и 50 для каждой строки. Это гарантирует,
#     что ярлык с текстом всегда отображает свой текст без обрезания каких-либо символов,
#     даже если размер окна очень мал.
#     '''
#
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#
#         label = tk.Label(master=frame, text=f'Row {i}\nColumn {j}')
#         label.pack(padx=5, pady=5)
#
# window.mainloop()

window = tk.Tk()

window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0)  # без заполнения ячейки. По умолчанию не используя STICKY
label2.grid(row=0, column=1, sticky="ew")  # заполнение ячейки по горизонтали
label3.grid(row=0, column=2, sticky="ns")  # заполнение ячейки по вертикали
label4.grid(row=0, column=3, sticky="nsew")  # заполнение всей ячейки

window.mainloop()