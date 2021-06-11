import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame()
frame2 = tk.Frame()

label1 = tk.Label(master=frame1, text="This is Frame 1")
label1.pack()

label2 = tk.Label(master=frame2, text="This is Frame 2")
label2.pack()

frame1.pack()
frame2.pack()


window.mainloop()