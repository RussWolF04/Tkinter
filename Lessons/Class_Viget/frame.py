import tkinter as tk

# Создаем окно
window = tk.Tk()

# Создаем рамки для "А" и "Б"
frame_a = tk.Frame()
frame_b = tk.Frame()

# Создаем ярлык для "А"
label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

# Создаем ярлык для "Б"
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

# Инициализируем "запускаем" виджет "А" и "Б"
frame_a.pack()
frame_b.pack()

# Запускаем наше окно с виджетами
window.mainloop()
