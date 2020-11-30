import tkinter as tk
from tkinter import *
from tkinter.ttk import *

root = tk.Tk()

h=900
w=1000

canvas = tk.Canvas(root, height=h, width=w)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=10)
frame.place(relx=0.1, rely=0.05, relwidth=0.6, relheight=0.4)


label1 = tk.Label(frame, text="1st Game", bg='green')
label1.place(x=8, y=100)

label2 = tk.Label(frame, text="2nd Game", bg='green')
label2.place(x=8, y=150)

label3 = tk.Label(frame, text="3rd Game", bg='green')
label3.place(x=8, y=200)

entry1 = tk.Entry(frame)
entry1.place(x=110, y=100)

entry2 = tk.Entry(frame, bg='pink')
entry2.place(x=110, y=150)

entry3 = tk.Entry(frame, bg='pink')
entry3.place(x=110, y=200)

button1 = tk.Button(frame, text ="Test Button", highlightbackground='blue', fg='brown', height=5, width=16)
button1.place(x=375, y=125)

lower_frame = tk.Frame(root, bg='#80c1aa',bd=5)
lower_frame.place(relx=0.1, rely=0.5, relwidth=0.5, relheight=0.2)

root.mainloop()