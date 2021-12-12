import tkinter as tk

window = tk.Tk()

# новый виджет рамки Frame
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

# создают новый ярлык с текстом под названием label1 с желтым фоном и помещает его в рамку frame1 на позицию (0, 0)
label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

# создают второй ярлык с текстом под названием label2 на красном фоне и помещают его в рамку frame1 на позицию (75, 75)
label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

window.mainloop()