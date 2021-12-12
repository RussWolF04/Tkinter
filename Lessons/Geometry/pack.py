import tkinter as tk

# window = tk.Tk()
#
# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack()
#
# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack()
#
# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack()
#
# window.mainloop()

# #
# window = tk.Tk()
#
# frame1 = tk.Frame(master=window, height=100, bg="white")
# frame1.pack(fill=tk.X)
#
# frame2 = tk.Frame(master=window, height=50, bg="blue")
# frame2.pack(fill=tk.X)
#
# frame3 = tk.Frame(master=window, height=25, bg="red")
# frame3.pack(fill=tk.X)
#
# window.mainloop()

window = tk.Tk()

# side
frame1 = tk.Frame(master=window, width=200, height=100, bg="red")  # аргумент height указываем высоту
# При установке аргумента fill=tk.X рамки адаптируются при горизонтальном изменении размера окна
frame1.pack(fill=tk.Y, side=tk.LEFT)  # аргумент fill=tk.Y они адаптируются при изменении размера окна по вертикали

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.Y, side=tk.LEFT)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.LEFT)

window.mainloop()

'''
Для того чтобы сделать макет по-настоящему адаптированным, можно установить начальный размер фреймов,
используя атрибуты width и height. Затем нужно установить значение аргумента fill от метода .pack() на tk.BOTH,
а также установить значение аргумента expand на True:
'''

window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()