import tkinter as tk
from tkinter.constants import TRUE

window = tk.Tk()

frame1 = tk.Frame()
frame2 = tk.Frame()

label1 = tk.Label(master=frame1, text="This is Frame 1", fg="black", bg="orange")
label1.pack(fill=tk.BOTH, expand=TRUE)

label2 = tk.Label(master=frame2, text="This is Frame 2", fg="green", bg="white")
label2.pack(fill=tk.BOTH, expand=TRUE)

frame1.pack(fill=tk.BOTH, expand=TRUE)
frame2.pack(fill=tk.BOTH, expand=TRUE)


window.mainloop()